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
            if query:
                url += f'&query={query}'
            if cuisine:
                url += f'&cuisine={cuisine}'
            if intolerances:
                url += f'&intolerances={intolerances}'
            if type:
                url += f'&type={type}'

            # Specify the number of results per page
            url += '&number=500'

            # Make a GET request to Spoonacular API
            response = requests.get(url)

            # Check if the response is successful
            if response.status_code == 200:
                # Extract recipe data from the response
                recipes = response.json()['results']

                # If no recipes found
                if not recipes:
                    # Return an error message. Redirects to search page
                    messages.error(request, "No recipes for this query. Try again")
                    return redirect("spoonacular_api:recipe_search")

                context = {'recipes': recipes}
                # Render the search results template with recipe data
                return render(request, "spoonacular_api/search_results.html", context)
            else:
                # Return an error message. Redirects to search page
                messages.error(request, "Failed to fetch recipes.")
                return redirect("spoonacular_api:recipe_search")
        else:
            # Form is invalid, return errors and go to search page
            messages.error(request, "Form is invalid.")
            return redirect("spoonacular_api:recipe_search")
    else:
        # If the request is not POST, render the form
        form = RecipeForm()
        return render(request, 'spoonacular_api/recipe_search.html', {'form': form})


def recipe_details(request, recipe_id):
    # Get Spoonacular API key from settings
    api_key = settings.SPOONACULAR_API_KEY

    # Construct the URL for fetching recipe details
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/priceBreakdownWidget.json?apiKey={api_key}"

    # Specify the number of results per page
    url += '&number=500'

    # Make a GET request to the Spoonacular API
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        # Extract detailed information from the response
        details = response.json()["ingredients"]

        # Extract image URL for each ingredient
        for ingredient in details:
            ingredient["image"] = f"https://spoonacular.com/cdn/ingredients_100x100/{ingredient['image']}"

        # Prepare context to pass to the template
        context = {'details': details}

        # Render the recipe details template with the recipe information
        return render(request, 'spoonacular_api/recipe_details.html', context)
    else:
        # If the response is not successful, display an error message and redirect to the recipe search page
        messages.error(request, "Failed to fetch recipe details.")
        return redirect("spoonacular_api:recipe_search")


