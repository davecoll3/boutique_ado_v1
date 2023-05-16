from django.contrib import admin
from .models import Recipes


class RecipesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'coffee_qty_g',
        'grind_size',
        'brew_time_mins',
    )

    ordering = ('name',)


admin.site.register(Recipes, RecipesAdmin)
