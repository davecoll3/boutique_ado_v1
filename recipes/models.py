from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from products.models import Product


class Recipes(models.Model):

    x_course = 'Extra-Course'
    coarse = 'Coarse'
    medium = 'Medium'
    m_fine = 'Medium-Fine'
    fine = 'Fine'
    s_fine = 'Superfine'

    GRIND = [
        (x_course, 'Extra-Course'),
        (coarse, 'Coarse'),
        (medium, 'Medium'),
        (m_fine, 'Medium-Fine'),
        (fine, 'Fine'),
        (s_fine, 'Superfine'),
    ]

    name = models.CharField(max_length=100)
    coffee_qty = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
        )
    grind_size = models.CharField(max_length=20, choices=GRIND, default=medium)
    water_temp = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    water_volume = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(999),
            MinValueValidator(1)
        ]
    )
    brew_time = models.DecimalField(max_digits=4, decimal_places=2)
    products = models.ManyToManyField(Product)
    method = models.TextField()

    def __str__(self):
        return self.name
