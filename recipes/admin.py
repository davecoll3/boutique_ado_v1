from django.contrib import admin
from .models import Recipes


class RecipesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'grind_size',
        'brew_time',
    )

    ordering = ('name',)


admin.site.register(Recipes, RecipesAdmin)
