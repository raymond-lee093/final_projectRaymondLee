from django import forms


class RecipeForm(forms.Form):
    query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Enter ingredient(s)", 'required': True, 'autofocus': True}))
    cuisine = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Enter cuisine type(s)"}))
    intolerances = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Enter dietary restriction(s)"}))
    type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Enter meal type(s)"}))