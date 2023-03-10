from django.urls import path

from sport_academy.views import (
    index,
    TeamListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("teams/", TeamListView.as_view(), name="teams-list")
]
app_name = "sport_academy"
