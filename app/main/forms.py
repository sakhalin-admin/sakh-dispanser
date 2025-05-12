from django import forms
from .models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ["name", "phone", "department", "position", "comment"]
        labels = {
            "name": "Имя",
            "phone": "Номер телефона",
            "department": "Отдел",
            "position": "Должность",
            "comment": "Комментарий",
        }
        widgets = {
            "phone": forms.TextInput(attrs={"type": "tel"}),
            "comment": forms.Textarea(attrs={"rows": 4}),
        }
