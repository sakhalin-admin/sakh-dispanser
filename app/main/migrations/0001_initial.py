# Generated by Django 5.2 on 2025-04-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('department', models.CharField(choices=[('Онкология', 'Онкология'), ('Химиотерапия', 'Химиотерапия'), ('Лучевая терапия', 'Лучевая терапия'), ('Педиатрия', 'Педиатрия'), ('Диагностика', 'Диагностика'), ('Хирургия', 'Хирургия')], max_length=50)),
                ('position', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
