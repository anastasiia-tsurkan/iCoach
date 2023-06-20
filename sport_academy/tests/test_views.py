from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from sport_academy.models import Club, Player

COACH_LIST_URL = reverse("sport_academy:coaches-list")
TEAM_LIST_URL = reverse("sport_academy:teams-list")
PLAYERS_LIST_URL = reverse("sport_academy:players-list")
CLUB_LIST_URL = reverse("sport_academy:clubs-list")
PAGINATION = 6


class CoachListTest(TestCase):
    fixtures = [
        "sport_club_db_data.json",
    ]

    def setUp(self):
        self.user = get_user_model().objects.get(id=1)
        self.client.force_login(self.user)

    def test_coach_list_response_with_correct_template(self):
        response = self.client.get(COACH_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sport_academy/coaches_list.html")

    def test_coaches_list_paginated_correctly(self):
        response = self.client.get(COACH_LIST_URL)

        self.assertEqual(
            len(response.context["coaches_list"]),
            PAGINATION
        )


class PlayersListTest(TestCase):
    fixtures = [
        "sport_club_db_data.json",
    ]

    def setUp(self):
        self.user = get_user_model().objects.get(id=1)
        self.client.force_login(self.user)

    def test_player_list_response_with_correct_template(self):
        response = self.client.get(PLAYERS_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sport_academy/players_list.html")

    def test_players_list_paginated_correctly(self):
        response = self.client.get(PLAYERS_LIST_URL)
        self.assertEqual(
            len(response.context["players_list"]),
            PAGINATION
        )

    def test_players_list_ordered_by_position_and_first_name(self):
        response = self.client.get(PLAYERS_LIST_URL)
        players_list = Player.objects.all().order_by("position", "first_name")
        players_context = response.context["players_list"]

        self.assertEqual(
            list(players_context),
            list(players_list[:len(players_context)])
        )


class ClubListTest(TestCase):
    fixtures = [
        "sport_club_db_data.json",
    ]

    def setUp(self):
        self.user = get_user_model().objects.get(id=1)
        self.client.force_login(self.user)

    def test_club_list_response_with_correct_template(self):
        response = self.client.get(CLUB_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sport_academy/clubs_list.html")

    def test_clubs_list_ordered_by_name(self):
        response = self.client.get(CLUB_LIST_URL)
        clubs_list = Club.objects.all().order_by("name")
        clubs_context = response.context["clubs_list"]

        self.assertEqual(
            list(clubs_context),
            list(clubs_list[:len(clubs_context)])
        )


class TeamListTest(TestCase):
    fixtures = [
        "sport_club_db_data.json",
    ]

    def setUp(self):
        self.user = get_user_model().objects.get(id=1)
        self.client.force_login(self.user)

    def test_team_list_response_with_correct_template(self):
        response = self.client.get(TEAM_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sport_academy/teams_list.html")

    def test_teams_list_paginated_correctly(self):
        response = self.client.get(TEAM_LIST_URL)

        self.assertEqual(
            len(response.context["teams_list"]),
            PAGINATION - 1
        )
