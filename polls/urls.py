from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_voter, name="register_voter"),
    path("stats/", views.voter_stats, name="voter_stats"),
]
