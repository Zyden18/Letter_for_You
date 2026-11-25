from django.db import models


class DateResponse(models.Model):
    class Answer(models.TextChoices):
        YES = "yes", "Yes"
        MAYBE_LATER = "maybe_later", "Maybe another time"

    answer = models.CharField(max_length=20, choices=Answer.choices)
    ideas = models.JSONField(default=list, blank=True)
    custom_idea = models.CharField(max_length=100, blank=True)
    preferred_day = models.DateField(null=True, blank=True)
    preferred_time = models.TimeField(null=True, blank=True)
    note = models.CharField(max_length=240, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "date response"
        verbose_name_plural = "date responses"

    def __str__(self):
        return f"{self.get_answer_display()} — {self.created_at:%Y-%m-%d %H:%M}"
