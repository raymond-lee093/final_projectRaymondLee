from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from . forms import RegistrationForm, AccountUpdateForm
from django.conf import settings
from . models import Account


def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Verify credentials, check against authentication backend
        # returns user object if credentials are valid
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login user
            login(request, user)
            return redirect("spoonacular_api:recipe_search")
        else:
            # Return an 'invalid login' error message. Redirects to login page
            messages.error(request, "Your username or password didn't match. Try again.")
            return redirect("account:login_user")
    else:
        return render(request, 'authentication/login.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, "User logged out.")
    return redirect("account:login_user")


def register_user(request, *args, **kwargs):
    # Check if the user is already authenticated
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.username) + ".")

    context = {}
    if request.POST:
        # If the request method is POST, process the form data
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the user
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Authenticate the user and log them in
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                # Redirect to the next URL if provided
                return redirect("destination")
            # Redirect to the search page after successful registration
            return redirect('spoonacular_api:recipe_search')
        else:
            # If the form is not valid, pass the form back to the template with errors
            context['registration_form'] = form
    else:
        # If the request method is not POST, render the empty registration form
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'authentication/register.html', context)


def account_view(request, *args, **kwargs):
    context = {}

    # Get the user_id from kwargs
    user_id = kwargs.get("user_id")

    # Fetch the account object using user_id
    try:
        account = Account.objects.get(pk=user_id)
    except:
        return HttpResponse("User does not exist.")

    # If account exists, set the context variables
    if account:
        context['id'] = account.id
        context['username'] = account.username
        context['email'] = account.email
        context['profile_image'] = account.profile_image.url
        context['hide_email'] = account.hide_email

        # Define template variables
        is_self = True
        is_friend = False
        user = request.user

        # Check if the user is authenticated and not the same as the viewed profile
        if user.is_authenticated and user != account:
            is_self = False
        elif not user.is_authenticated:
            is_self = False

        # Set the template variables to the values
        context['is_self'] = is_self
        context['is_friend'] = is_friend
        context['BASE_URL'] = settings.BASE_URL

        # Render the account.html template with the context
        return render(request, "authentication/account.html", context)


def edit_account_view(request, *args, **kwargs):

    # View for editing the user account details.

    # Redirect to login page if user is not authenticated
    if not request.user.is_authenticated:
        return redirect("account:login_user")

    # Retrieve the user's account
    user_id = kwargs.get("user_id")
    account = Account.objects.get(pk=user_id)

    # Check if the user is trying to edit someone else's profile
    if account.pk != request.user.pk:
        return HttpResponse("You cannot edit someone else's profile.")

    context = {}
    if request.POST:
        # Process the form data
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            new_username = form.cleaned_data['username']
            # Redirect to the user's profile page after successful update
            return redirect("account:account_view", user_id=account.pk)
        else:
            # If form is not valid, render the form again with errors
            form = AccountUpdateForm(
                                     initial={
                                         "id": account.pk,
                                         "email": account.email,
                                         "username": account.username,
                                         "profile_image": account.profile_image,
                                         "hide_email": account.hide_email,
                                     }
                                     )
            context['form'] = form
    else:
        # Render the form with initial data
        form = AccountUpdateForm(
            initial={
                "id": account.pk,
                "email": account.email,
                "username": account.username,
                "profile_image": account.profile_image,
                "hide_email": account.hide_email,
            }
        )
        context['form'] = form
    # Setting the max data size of an image
    context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
    return render(request, "authentication/edit_account.html", context)