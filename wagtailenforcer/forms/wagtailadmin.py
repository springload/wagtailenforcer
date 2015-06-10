from django import forms


class SearchForm(forms.Form):
    """
    Extremely simple form with only a search text input
    """
    search_field = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search Text'})
    )
