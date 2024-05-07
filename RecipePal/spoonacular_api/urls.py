from django.urls import path
from . import views

app_name = 'spoonacular_api'
urlpatterns = [
     path("recipe_search", views.recipe_search, name='recipe_search'),
]