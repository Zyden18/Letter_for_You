from datetime import date, time

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render

from .models import DateResponse

DATE_IDEAS = [
    "Coffee or a cute café",
    "Dinner somewhere yummy",
    "A movie night",
    "A little outdoor adventure",
    "Dessert and a sweet treat",
    "A surprise date",
]


def invitation(request):
    if request.method == "POST":
        answer = request.POST.get("answer")
        if answer == DateResponse.Answer.MAYBE_LATER:
            DateResponse.objects.create(answer=answer)
            request.session.pop("date_plan", None)
            return redirect("thanks")
        if answer == DateResponse.Answer.YES:
            request.session["date_plan"] = {"answer": answer}
            return redirect("ideas")
    return render(request, "invitations/invitation.html")


def _plan_or_start_over(request):
    plan = request.session.get("date_plan")
    if not plan:
        return None
    return plan


def ideas(request):
    plan = _plan_or_start_over(request)
    if plan is None:
        return redirect("invitation")
    if request.method == "POST":
        selected = request.POST.getlist("ideas")
        plan["ideas"] = [idea for idea in selected if idea in DATE_IDEAS]
        plan["custom_idea"] = request.POST.get("custom_idea", "").strip()[:100]
        if not plan["ideas"] and not plan["custom_idea"]:
            return render(request, "invitations/ideas.html", {
                "date_ideas": DATE_IDEAS,
                "plan": plan,
                "error": "Please choose at least one date idea or write your own before continuing.",
            })
        request.session["date_plan"] = plan
        return redirect("schedule")
    return render(request, "invitations/ideas.html", {"date_ideas": DATE_IDEAS, "plan": plan})


def schedule(request):
    plan = _plan_or_start_over(request)
    if plan is None:
        return redirect("invitation")
    if request.method == "POST":
        plan["preferred_day"] = request.POST.get("preferred_day", "")
        plan["preferred_time"] = request.POST.get("preferred_time", "")
        request.session["date_plan"] = plan
        return redirect("note")
    return render(request, "invitations/schedule.html", {"plan": plan})


def note(request):
    plan = _plan_or_start_over(request)
    if plan is None:
        return redirect("invitation")
    if request.method == "POST":
        plan["note"] = request.POST.get("note", "").strip()[:240]
        request.session["date_plan"] = plan
        return redirect("review")
    return render(request, "invitations/note.html", {"plan": plan})


def review(request):
    plan = _plan_or_start_over(request)
    if plan is None:
        return redirect("invitation")
    if request.method == "POST":
        day = date.fromisoformat(plan["preferred_day"]) if plan.get("preferred_day") else None
        preferred_time = time.fromisoformat(plan["preferred_time"]) if plan.get("preferred_time") else None
        DateResponse.objects.create(
            answer=DateResponse.Answer.YES,
            ideas=plan.get("ideas", []),
            custom_idea=plan.get("custom_idea", ""),
            preferred_day=day,
            preferred_time=preferred_time,
            note=plan.get("note", ""),
        )
        request.session.pop("date_plan", None)
        return redirect("thanks")
    return render(request, "invitations/review.html", {"plan": plan})


def thanks(request):
    return render(request, "invitations/thanks.html")


@staff_member_required
def response_list(request):
    return render(request, "invitations/responses.html", {"responses": DateResponse.objects.all()})
