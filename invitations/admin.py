from django.contrib import admin

from .models import DateResponse


@admin.register(DateResponse)
class DateResponseAdmin(admin.ModelAdmin):
    list_display = ("answer", "preferred_day", "preferred_time", "created_at")
    list_filter = ("answer", "created_at")
    search_fields = ("custom_idea", "note")
    readonly_fields = ("created_at",)
