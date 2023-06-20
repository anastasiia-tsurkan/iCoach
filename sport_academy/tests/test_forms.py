from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from sport_academy.models import Player


class DriverTest(TestCase):
    fixtures = [
        "sport_club_db_data.json"
    ]

    def setUp(self):
        self.user = get_user_model().objects.get(id=1)
        self.client.force_login(self.user)

    def test_search_form_players_by_last_name(self):
        response = self.client.get(
            reverse("sport_academy:players-list") + "?last_name=M"
        )

        self.assertEqual(
            list(response.context["players_list"]),
            list(Player.objects.filter(last_name__icontains="M"))
        )
