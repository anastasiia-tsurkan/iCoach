from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from sport_academy.models import Club, Coach, Player, Team


def index(request):
    """View function for the home page of the site"""
    num_teams = Team.objects.count()
    num_coaches = Coach.objects.count() - 1
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


"""Player views"""


class TeamCreateView(generic.CreateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("sport_academy:teams-list")


class TeamDetailView(generic.DetailView):
    model = Team


class TeamUpdateView(generic.UpdateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("sport_academy:teams-list")


class TeamDeleteView(generic.DeleteView):
    model = Team
    success_url = reverse_lazy("sport_academy:teams-list")


"""Player views"""


class PlayersListView(generic.ListView):
    model = Player
    context_object_name = "players_list"
    template_name = "sport_academy/players_list.html"
    paginate_by = 10
    queryset = Player.objects.all()


class PlayerDetailView(generic.DetailView):
    model = Player


class PlayerCreateView(generic.CreateView):
    model = Player
    fields = "__all__"
    success_url = reverse_lazy("sport_academy:players-list")


class PlayerUpdateView(generic.UpdateView):
    model = Player
    fields = "__all__"
    success_url = reverse_lazy("sport_academy:players-list")


class PlayerDeleteView(generic.DeleteView):
    model = Player
    success_url = reverse_lazy("sport_academy:players-list")


"""Coach views"""


class CoachListView(generic.ListView):
    model = Coach
    context_object_name = "coaches_list"
    template_name = "sport_academy/coaches_list.html"
    paginate_by = 5
    queryset = Coach.objects.all()


class CoachDetailView(generic.DetailView):
    model = Coach


"""Club views"""
