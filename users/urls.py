from django.urls import path

from . import views

urlpatterns = [
    path("", views.auth_login, name="login"),
    path("logout", views.auth_logout, name="logout"),
    path("register", views.register, name="register")
]