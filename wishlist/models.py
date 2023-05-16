from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    """ Wishlist model to store users favourite products"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
