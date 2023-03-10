from django.urls import path

from sport_academy.views import (
    index,
    TeamListView,
    TeamDetailView,
    TeamCreateView,
    TeamUpdateView,
    TeamDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("teams/", TeamListView.as_view(), name="teams-list"),
    path("teams/create/", TeamCreateView.as_view(), name="team-create"),
    path("team/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("team/<int:pk>/update/", TeamUpdateView.as_view(), name="team-update"),
    path("team/<int:pk>/delete/", TeamDeleteView.as_view(), name="team-delete"),


]
app_name = "sport_academy"
