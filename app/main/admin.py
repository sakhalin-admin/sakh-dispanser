from django.contrib import admin
from .models import Submission


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "department", "position", "submitted_at")
    search_fields = ("name", "department", "position")
    list_filter = ("department", "submitted_at")
