from datetime import date
from django.test import TestCase

from sport_academy.models import Player, Team, Club, Coach, Position


class ModelsTests(TestCase):
    def setUp(self):
        position_ = Position.objects.create(position_name="halfback")
        club_ = Club.objects.create(
            name="Juventus",
            country="Italy",
            city="Turin",
            main_stadium="Allianz stadium"
        )
        team_ = Team.objects.create(
            name="First",
            status="Adult",
            league="Serie A",
            season="2022/23",
            club=club_
        )
        Coach.objects.create(
            position="Manager",
        )
        Player.objects.create(
            first_name="Paul",
            last_name="Pogba",
            birth_date=date(1993, 3, 15),
            number=10,
            position=position_,
            nationality="French",
            team=team_,
        )

    def test_team_str(self):
        team_test = Team.objects.get(id=1)
        self.assertEqual(str(team_test), "Juventus First team")

    def test_number_of_players_in_a_team(self):
        test_team = Team.objects.get(id=1)
        self.assertEqual(test_team.num_of_players, 1)
