from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
        )
        self.client.force_login(self.admin_user)
        self.coach = get_user_model().objects.create_user(
            username="Coach",
            password="coach12345",
            position="Manager",
        )

    def test_coach_position_listed(self):

        url = reverse("admin:sport_academy_coach_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.coach.position)
