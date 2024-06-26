from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("register_user", views.register_user, name="register_user"),
    path("<user_id>", views.account_view, name="account_view"),
    path("<user_id>/edit", views.edit_account_view, name="edit_account_view"),
]