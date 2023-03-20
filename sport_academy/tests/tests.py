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


