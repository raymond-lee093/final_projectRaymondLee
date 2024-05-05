from django import forms
from django.contrib.auth.forms import UserCreationForm

from . models import Account


class RegistrationForm(UserCreationForm):
    # Custom registration form with additional email field
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        # Define the model and fields for the form
        model = Account
        fields = ('email', 'username', 'password1', 'password2', )

    def clean_email(self):
        # Clean and validate the email field
        email = self.cleaned_data['email'].lower()
        try:
            # Check if the email is already in use
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            # If email is unique, return it
            return email
        # If email is not unique, raise a validation error
        raise forms.ValidationError('Email "%s" is already in use.' % email)

    def clean_username(self):
        # Clean and validate the username field
        username = self.cleaned_data['username']
        try:
            # Check if the username is already in use
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            # If username is unique, return it
            return username
        # If username is not unique, raise a validation error
        raise forms.ValidationError('Username "%s" is already in use.' % username)
