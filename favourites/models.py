from django.db import models

from products.models import Product
from profiles.models import UserProfile


class FavouritesList(models.Model):
    # Links favourites list to user's profile
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='favourites_user')

    def __str__(self):
        return f"{self.user}'s favourites"


class FavouritesListItem(models.Model):
    # Links items to user's favourites list
    favourites = models.ForeignKey(FavouritesList, on_delete=models.CASCADE, related_name='favourites_list')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='favourite_products')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
