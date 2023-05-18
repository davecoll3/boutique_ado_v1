from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    # Model to show all product items within the users wishlist
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user}'s Wishlist"
