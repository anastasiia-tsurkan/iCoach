from django import forms
from datetime import date

from django.core.validators import MinValueValidator

from sport_academy.models import Player


class PlayerSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by last name..."})
    )


class PlayerForm(forms.ModelForm):
    MIN_BIRTH_DATE = date(1950, 1, 1)

    birth_date = forms.DateField(
        required=True,
        validators=[MinValueValidator(MIN_BIRTH_DATE)]
    )

    class Meta:
        model = Player
        fields = "__all__"
