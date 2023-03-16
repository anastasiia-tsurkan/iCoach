from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from sport_academy.models import Club, Coach, Player, Team


def index(request):
    """View function for the home page of the site"""

    return render(
        request,
        "sport_academy/index.html",
    )


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    context_object_name = "teams_list"
    template_name = "sport_academy/teams_list.html"
    paginate_by = 5
    queryset = Team.objects.select_related("club")


"""Player views"""


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("sport_academy:teams-list")


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("sport_academy:teams-list")


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    success_url = reverse_lazy("sport_academy:teams-list")


"""Player views"""


class PlayersListView(LoginRequiredMixin, generic.ListView):
    model = Player
    context_object_name = "players_list"
    template_name = "sport_academy/players_list.html"
    paginate_by = 6
    queryset = Player.objects.select_related("team")


class PlayerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Player


class PlayerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Player
    fields = "__all__"
    success_url = reverse_lazy("sport_academy:players-list")


class PlayerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Player
    fields = "__all__"
    success_url = reverse_lazy("sport_academy:players-list")


class PlayerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Player
    success_url = reverse_lazy("sport_academy:players-list")


"""Coach views"""


class CoachListView(LoginRequiredMixin, generic.ListView):
    model = Coach
    context_object_name = "coaches_list"
    template_name = "sport_academy/coaches_list.html"
    paginate_by = 5
    queryset = Coach.objects.prefetch_related("team")


class CoachDetailView(LoginRequiredMixin, generic.DetailView):
    model = Coach


"""Club views"""


class ClubListView(LoginRequiredMixin, generic.ListView):
    model = Club
    context_object_name = "clubs_list"
    template_name = "sport_academy/clubs_list.html"
    queryset = Club.objects.all()


class ClubDetailView(LoginRequiredMixin, generic.DetailView):
    model = Club
