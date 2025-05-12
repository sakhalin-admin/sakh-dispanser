from django.urls import path
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView


from main import views

app_name = "main"


def simple_logout(request):
    logout(request)
    return redirect("main:login")


def dummy_logout(request):
    return redirect("main:login")


urlpatterns = [
    path("", views.main, name="main"),
    path("contacts/", views.contacts, name="contacts"),
    path("ustav/", views.ustav, name="ustav"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("form/", views.form, name="form"),
    path("review/", views.review_submissions, name="review_submissions"),
    path("logout/", views.custom_logout, name="logout"),
    path(
        "review/delete/<int:submission_id>/",
        views.delete_submission,
        name="delete_submission",
    ),
    path(
        "review/edit/<int:submission_id>/",
        views.edit_submission,
        name="edit_submission",
    ),
    path("review/comment/<int:submission_id>/", views.add_comment, name="add_comment"),
]
