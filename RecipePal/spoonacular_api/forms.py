from django import forms


class RecipeForm(forms.Form):
    # Fields are required by default
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Enter ingredient(s)", 'autofocus': True}))
    cuisine = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Enter cuisine type(s)"}))
    intolerances = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Enter dietary restriction(s)"}))
    type = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Enter meal type(s)"}))
