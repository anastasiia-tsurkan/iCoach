from django.urls import path

from sport_academy.views import (
    index,
    TeamListView,
    TeamCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("teams/", TeamListView.as_view(), name="teams-list"),
    path("teams/create/", TeamCreateView.as_view(), name="team-create"),
    
]
app_name = "sport_academy"
