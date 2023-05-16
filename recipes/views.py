from django.shortcuts import render
from .models import Recipes


def all_recipes(request):
    """ A view to return all brewing recipies """

    recipes = Recipes.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'recipes/recipes.html', context)