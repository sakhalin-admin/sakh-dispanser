from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth import logout
from .models import Submission
from .forms import SubmissionForm
from django.utils.timezone import now, localtime


# Create your views here.
def main(request):
    return render(request, "main/main.html")


def contacts(request):
    return render(request, "main/contacts.html")


def ustav(request):
    return render(request, "main/ustav.html")


def login(request):
    return render(request, "main/login.html")


def custom_logout(request):
    logout(request)
    return redirect("main:login")


@login_required
def form(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка успешно отправлена.")
            return redirect("main:form")
    else:
        form = SubmissionForm()

    return render(request, "form.html", {"form": form})


@staff_member_required
def review_submissions(request):
    submissions = Submission.objects.order_by("-submitted_at")
    return render(request, "review.html", {"submissions": submissions})


@staff_member_required
def delete_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    submission.delete()
    messages.success(request, "Заявка удалена.")
    return redirect("main:review_submissions")


@staff_member_required
def edit_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    if request.method == "POST":
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка обновлена.")
            return redirect("main:review_submissions")
    else:
        form = SubmissionForm(instance=submission)
    return render(request, "edit_submission.html", {"form": form})


@staff_member_required
def add_comment(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    if request.method == "POST":
        comment = request.POST.get("comment")
        admin_username = request.user.username
        timestamp = localtime(now()).strftime("%d.%m.%Y %H:%M")
        styled_comment = (
            f'\n\n<div class="admin-comment-box">'
            f'<span class="admin-comment-text">{admin_username}: {comment}</span>'
            f'<span class="admin-comment-date">{timestamp}</span>'
            f"</div>"
        )
        submission.comment += styled_comment
        submission.save()
        messages.success(request, "Комментарий добавлен.")
        return redirect("main:review_submissions")
    return render(request, "add_comment.html", {"submission": submission})
