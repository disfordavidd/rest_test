from django.urls import path

from test_app import views

urlpatterns = [
    path("users/", views.index, name="index"),
]