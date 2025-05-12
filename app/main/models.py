from django.db import models


class Submission(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    DEPARTMENT_CHOICES = [
        ("Онкология", "Онкология"),
        ("Химиотерапия", "Химиотерапия"),
        ("Лучевая терапия", "Лучевая терапия"),
        ("Педиатрия", "Педиатрия"),
        ("Диагностика", "Диагностика"),
        ("Хирургия", "Хирургия"),
    ]
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)

    position = models.CharField(max_length=100)
    comment = models.TextField(blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.department})"
