from django.test import TestCase
from django.contrib.auth import get_user_model
from newspaper.forms import (
    RedactorCreationForm,
    RedactorUpdateForm,
    NewspaperForm,
    RedactorSearchForm,
    TopicSearchForm,
    NewspaperSearchForm,
)


class RedactorCreationFormTests(TestCase):
    def test_valid_data(self):
        form = RedactorCreationForm({
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'years_of_experience': 5,
            'first_name': 'John',
            'last_name': 'Doe',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_years_of_experience_negative(self):
        form = RedactorCreationForm({
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'years_of_experience': -1,
            'first_name': 'John',
            'last_name': 'Doe',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['years_of_experience'],
            ['Years of experience must be greater or equal than 0']
        )

    def test_invalid_years_of_experience_greater_than_100(self):
        form = RedactorCreationForm({
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'years_of_experience': 101,
            'first_name': 'John',
            'last_name': 'Doe',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['years_of_experience'],
            ['Please, provide correct data']
        )

class RedactorUpdateFormTests(TestCase):
    def test_valid_data(self):
        redactor = get_user_model().objects.create(username='testuser', password='testpassword')
        form = RedactorUpdateForm({
            'years_of_experience': 5,
            'first_name': 'John',
            'last_name': 'Doe',
        }, instance=redactor)
        self.assertTrue(form.is_valid())

    def test_invalid_years_of_experience_negative(self):
        form = RedactorCreationForm({
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'years_of_experience': -1,
            'first_name': 'John',
            'last_name': 'Doe',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['years_of_experience'],
            ['Years of experience must be greater or equal than 0']
        )

    def test_invalid_years_of_experience_greater_than_100(self):
        redactor = get_user_model().objects.create(username='testuser', password='testpassword')
        form = RedactorUpdateForm({
            'years_of_experience': 101,
            'first_name': 'John',
            'last_name': 'Doe',
        }, instance=redactor)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['years_of_experience'],
            ['Please, provide correct data']
        )


class NewspaperFormTests(TestCase):
    def test_invalid_data(self):
        form = NewspaperForm({
            'title': 'Test Newspaper',
            'publishers': [999],  # Invalid user ID
            'topic': 'Test Topic',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['publishers'],
            ['Select a valid choice. 999 is not one of the available choices.']
        )

class RedactorSearchFormTests(TestCase):
    def test_valid_data(self):
        form = RedactorSearchForm({
            'username': 'testuser',
        })
        self.assertTrue(form.is_valid())

class TopicSearchFormTests(TestCase):
    def test_valid_data(self):
        form = TopicSearchForm({
            'name': 'Test Topic',
        })
        self.assertTrue(form.is_valid())

class NewspaperSearchFormTests(TestCase):
    def test_valid_data(self):
        form = NewspaperSearchForm({
            'title': 'Test Newspaper',
        })
        self.assertTrue(form.is_valid())
