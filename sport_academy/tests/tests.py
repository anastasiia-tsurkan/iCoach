from datetime import datetime

from django.test import TestCase

from sport_academy.models import Player, Position, Team, Club


class PlayerModelTest(TestCase):
    def setUp(self):
        test_position = Position.objects.create(position_name="test position")
        test_club = Club.objects.create(
            name="Test club",
            country="Test country",
            city="Test city",
            main_stadium="Test stadium"
        )
        test_team = Team.objects.create(
            name="Test name",
            status="Test status",
            league="Test league",
            season="Test seasson",
            club=test_club
        )
        Player.objects.create(
            first_name="Test first",
            last_name="Test last",
            birth_date="1999-01-01",
            number="10",
            position=test_position,
            nationality="Test nationality",
            picture_url="/images/avatar.png",
            team=test_team
        )

    def test_property_player_age_count(self):
        test_player = Player.objects.get(id=1)
        age = datetime.today().year - test_player.birth_date.year
        self.assertEqual(age, test_player.age)
