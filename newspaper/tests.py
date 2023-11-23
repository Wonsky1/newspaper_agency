from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper.models import Topic, Redactor, Newspaper


class ModelTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="teststr")
        self.assertEqual(str(topic), topic.name)

    def test_redactor_str(self):
        redactor = get_user_model().objects.create_user(
            username="test3214",
            password="test",
        )
        self.assertEqual(str(redactor), "test3214")

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="teststr")
        newspaper = Newspaper.objects.create(
            title="title",
            content="content",
            topic=topic,
        )
        self.assertEqual(str(newspaper), newspaper.title)

    def test_create_redactor_with_years_of_experience(self):
        expected = 2
        redactor = get_user_model().objects.create_user(
            username="test3214",
            password="test",
            years_of_experience=expected
        )
        self.assertEqual(redactor.years_of_experience, expected)

    def test_create_redactor_without_years_of_experience(self):
        raw_password = "test"
        redactor = get_user_model().objects.create_user(
            username="test3214",
            password=raw_password,
        )
        self.assertEqual(redactor.years_of_experience, 0)
        self.assertTrue(redactor.check_password(raw_password))

