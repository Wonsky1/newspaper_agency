from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from newspaper.models import Topic, Newspaper


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="admin1234"
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="redactor", password="redactor1234", years_of_experience=1
        )
        self.topic = Topic.objects.create(name="Test Topic")
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper", topic=self.topic
        )

    def test_redactor_admin_page(self):
        response = self.client.get(reverse("admin:newspaper_redactor_changelist"))
        self.assertEqual(response.status_code, 200)

    def test_newspaper_admin_page(self):
        response = self.client.get(reverse("admin:newspaper_newspaper_changelist"))
        self.assertEqual(response.status_code, 200)

    def test_topic_admin_page(self):
        url = reverse("admin:newspaper_topic_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_redactor_years_of_experience_listed(self) -> None:
        url = reverse("admin:newspaper_redactor_changelist")
        response = self.client.get(url)

        self.assertContains(response, str(self.redactor.years_of_experience))

    def test_redactor_detail_years_of_experience_listed(self):
        url = reverse("admin:newspaper_redactor_change", args=[self.redactor.pk])
        response = self.client.get(url)

        self.assertContains(response, str(self.redactor.years_of_experience))

    def test_newspaper_admin_search(self):
        url = reverse("admin:newspaper_newspaper_changelist")
        response = self.client.get(url, {"q": "Test Newspaper"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Newspaper")

    def test_newspaper_admin_filter(self):
        url = reverse("admin:newspaper_newspaper_changelist")
        response = self.client.get(url, {"topic__id__exact": self.topic.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Newspaper")
