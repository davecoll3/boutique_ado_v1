from django.contrib import admin
from .models import FavouritesList, FavouritesListItem


class FavouritesAdmin(admin.ModelAdmin):
    # Admin for FavouritesListItem
    model = FavouritesListItem
    readonly_fields = ('added_on',)
    fields = ('favourites', 'product', 'added_on',)
    list_display = ('favourites', 'product', 'added_on',)
    ordering = ('favourites',)


admin.site.register(FavouritesList)
admin.site.register(FavouritesListItem, FavouritesAdmin)
