from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from . forms import RegistrationForm


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
            return redirect("main:index")
        else:
            # Return an 'invalid login' error message. Redirects to login page
            messages.error(request, "Your username or password didn't match. Try again.")
            return redirect("account:login_user")
    else:
        return render(request, "authentication/login.html", context)


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
            # Redirect to the home page after successful registration
            return redirect('main:index')
        else:
            # If the form is not valid, pass the form back to the template with errors
            context['registration_form'] = form
    else:
        # If the request method is not POST, render the empty registration form
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, "authentication/register.html", context)