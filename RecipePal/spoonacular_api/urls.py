from django.urls import path
from . import views

app_name = 'spoonacular_api'
urlpatterns = [
     path("recipe_search", views.recipe_search, name='recipe_search'),
     path('recipe_details/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
]