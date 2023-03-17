from django import forms


class PlayerSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=67,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by last name..."})
    )
