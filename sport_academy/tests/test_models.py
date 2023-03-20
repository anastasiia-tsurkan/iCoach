from datetime import date

from django.core.exceptions import ValidationError
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
            first_name="Max",
            last_name="Allegri",
            position="Manager",
            birth_date=date(1970, 1, 1)
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

    """Team model"""

    def test_number_of_players_in_a_team(self):
        test_team = Team.objects.get(id=1)
        self.assertEqual(test_team.num_of_players, 1)

    def test_team_str(self):
        team_test = Team.objects.get(id=1)
        self.assertEqual(str(team_test), "Juventus First team")

    """Player model tests"""

    def test_player_str(self):
        player_ = Player.objects.get(id=1)
        self.assertEqual(str(player_), "Paul Pogba (halfback)")

    def test_property_player_age_count(self):
        test_player = Player.objects.get(id=1)
        age = date.today().year - test_player.birth_date.year - (test_player.birth_date >= date.today())
        self.assertEqual(age, test_player.age)

    """Club model test"""

    def test_club_str(self):
        club_ = Club.objects.get(id=1)
        self.assertEqual(str(club_), "Juventus Turin")

    """Position model"""

    def test_position_str(self):
        position_ = Position.objects.get(id=1)
        self.assertEqual(str(position_), "halfback")

    """Coach model"""

    def test_coach_str(self):
        coach_ = Coach.objects.get(id=1)
        self.assertEqual(str(coach_), "Max Allegri")

    def test_property_coach_age_count(self):
        coach_ = Coach.objects.get(id=1)
        age = date.today().year - coach_.birth_date.year - (coach_.birth_date >= date.today())
        self.assertEqual(age, coach_.age)
