from django.urls import path

from sport_academy.views import (
    index,
    TeamListView,
    TeamDetailView,
    TeamCreateView,
    TeamUpdateView,
    TeamDeleteView,
    toggle_coach_assign_to_team,
    PlayersListView,
    PlayerDetailView,
    PlayerCreateView,
    PlayerUpdateView,
    PlayerDeleteView,
    CoachListView,
    CoachDetailView,
    ClubListView,
    ClubDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("teams/", TeamListView.as_view(), name="teams-list"),
    path("teams/create/", TeamCreateView.as_view(), name="team-create"),
    path("team/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("team/<int:pk>/update/", TeamUpdateView.as_view(), name="team-update"),
    path("team/<int:pk>/delete/", TeamDeleteView.as_view(), name="team-delete"),
    path("team/<int:pk>/toggle_assign/", toggle_coach_assign_to_team, name="toggle_coach_team_assign"),
    path("players/", PlayersListView.as_view(), name="players-list"),
    path("player/<int:pk>/", PlayerDetailView.as_view(), name="player-detail"),
    path("player/create/", PlayerCreateView.as_view(), name="player-create"),
    path("player/<int:pk>/update/", PlayerUpdateView.as_view(), name="player-update"),
    path("player/<int:pk>/delete/", PlayerDeleteView.as_view(), name="player-delete"),
    path("coaches/", CoachListView.as_view(), name="coaches-list"),
    path("coach/<int:pk>/", CoachDetailView.as_view(), name="coach-detail"),
    path("clubs/", ClubListView.as_view(), name="clubs-list"),
    path("club/<int:pk>/", ClubDetailView.as_view(), name="club-detail"),


]
app_name = "sport_academy"
