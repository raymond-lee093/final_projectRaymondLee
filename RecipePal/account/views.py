from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
