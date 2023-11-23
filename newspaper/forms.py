from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from newspaper.models import Redactor, Newspaper


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_years_of_experience(self) -> int:
        return cleaned_years_of_experience(self.cleaned_data["years_of_experience"])


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_years_of_experience(self) -> int:
        return cleaned_years_of_experience(self.cleaned_data["years_of_experience"])


def cleaned_years_of_experience(years_of_experience) -> int:
    if years_of_experience < 0:
        raise ValidationError("Years of experience must be greater or equal then 0")
    if years_of_experience > 100:
        raise ValidationError("Please, provide correct data")
    return years_of_experience


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"
