from django.contrib import admin
from django.urls import path

from invitations import views

urlpatterns = [
    path("", views.invitation, name="invitation"),
    path("ideas/", views.ideas, name="ideas"),
    path("schedule/", views.schedule, name="schedule"),
    path("note/", views.note, name="note"),
    path("review/", views.review, name="review"),
    path("thanks/", views.thanks, name="thanks"),
    path("responses/", views.response_list, name="response_list"),
    path("admin/", admin.site.urls),
]
