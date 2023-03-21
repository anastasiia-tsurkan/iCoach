from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from sport_academy.forms import PlayerSearchForm, PlayerForm
from sport_academy.models import Club, Coach, Player, Team


def index(request):
    """View function for the home page of the site"""

    return render(
        request,
        "sport_academy/index.html",
    )


"""Team views"""


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    context_object_name = "teams_list"
    template_name = "sport_academy/teams_list.html"
    paginate_by = 5
    queryset = Team.objects.select_related("club")


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(
            PlayersListView, self
        ).get_context_data(**kwargs)

        player_last_name = self.request.GET.get("last_name",)
        context["search_form"] = PlayerSearchForm(
            initial={"last_name": player_last_name}
        )
        return context

    def get_queryset(self) -> QuerySet:
        player_last_name = self.request.GET.get("last_name")

        if player_last_name:
            return self.queryset.filter(last_name__icontains=player_last_name)
        return self.queryset


class PlayerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Player


class PlayerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy("sport_academy:players-list")


class PlayerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy("sport_academy:players-list")


class PlayerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Player
    success_url = reverse_lazy("sport_academy:players-list")


"""Coach views"""


class CoachListView(LoginRequiredMixin, generic.ListView):
    model = Coach
    context_object_name = "coaches_list"
    template_name = "sport_academy/coaches_list.html"
    paginate_by = 6
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


class ClubCreateView(LoginRequiredMixin, generic.CreateView):
    model = Club
    fields = "__all__"
    success_url = reverse_lazy("sport_academy:clubs-list")


"""Additional functions"""


@login_required
def toggle_coach_assign_to_team(request, pk) -> HttpResponseRedirect:
    coach = Coach.objects.get(id=request.user.id)
    if (
        Team.objects.get(id=pk) in coach.team.all()
    ):
        coach.team.remove(pk)
    else:
        coach.team.add(pk)
    return HttpResponseRedirect(reverse_lazy("sport_academy:team-detail", args=[pk]))
