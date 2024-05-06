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


class AccountUpdateForm(forms.ModelForm):
    # Form for updating account details.
    class Meta:
        model = Account
        fields = ('username', 'email', 'profile_image', 'hide_email' )

    def clean_email(self):
        # Check if the provided email is unique.
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        # Check if the provided username is unique.
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)

    def save(self, commit=True):
        # Save the form data to the Account model.
        account = super(AccountUpdateForm, self).save(commit=False)
        account.username = self.cleaned_data['username']
        account.email = self.cleaned_data['email'].lower()
        account.profile_image = self.cleaned_data['profile_image']
        account.hide_email = self.cleaned_data['hide_email']
        if commit:
            account.save()
        return account