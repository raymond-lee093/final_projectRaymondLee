from django.urls import path
from . import views

app_name = 'spoonacular_api'
urlpatterns = [
     path("home", views.home, name="home"),
     path("recipe_search", views.recipe_search, name='recipe_search'),
]