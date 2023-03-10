from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from sport_academy.models import Club, Coach, Player, Team


def index(request):
    """View function for the home page of the site"""
    num_teams = Team.objects.count()
    num_coaches = Coach.objects.count()
    num_players = Player.objects.count()

    context = {
        "num_coaches": num_coaches,
        "num_teams": num_teams,
        "num_players": num_players,
    }

    return render(
        request,
        "sport_academy/index.html",
        context=context
    )


class TeamListView(generic.ListView):
    model = Team
    context_object_name = "teams_list"
    template_name = "sport_academy/teams_list.html"
    paginate_by = 5
    queryset = Team.objects.all()

    # def count_number_of_players_in_the_team(self, team_id: int):
    #     return Team.objects.get(id=team_id).count()


class TeamCreateView(generic.CreateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("sport_academy:teams-list")


