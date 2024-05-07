from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RecipeForm
import requests
from django.conf import settings


def recipe_search(request):
    if request.method == 'POST':
        # Get the form data
        form = RecipeForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Get the cleaned data from the form
            query = form.cleaned_data['query']
            cuisine = form.cleaned_data['cuisine']
            intolerances = form.cleaned_data['intolerances']
            type = form.cleaned_data['type']

            # Get API key from settings
            api_key = settings.SPOONACULAR_API_KEY
            # Construct the base URL for the API request
            url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}"

            # Construct the URL with search parameters from form
            url += f'&query={query}'
            url += f'&cuisine={cuisine}'
            url += f'&intolerances={intolerances}'
            url += f'&type={type}'

            # Make a GET request to Spoonacular API
            response = requests.get(url)

            # Check if the response is successful
            if response.status_code == 200:
                # Extract recipe data from the response
                recipes = response.json()['results']
                context = {'recipes': recipes}
                # Render the search results template with recipe data
                return render(request, "templates/spoonacular", context)
            else:
                # Return an error message. Redirects to homepage
                messages.error(request, "Failed to fetch recipes.")
                return redirect("main:index")
        else:
            # Form is invalid, return errors and go to homepage
            messages.error(request, "Form is invalid.")
            return redirect("main:index")
    else:
        # If the request is not POST, render the form
        form = RecipeForm()
        return render(request, 'main/index.html', {'form': form})
