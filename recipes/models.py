from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from products.models import Product


class Recipes(models.Model):

    class Meta:
        verbose_name_plural = 'Recipes'

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
    coffee_qty_g = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
        )
    grind_size = models.CharField(max_length=20, choices=GRIND, default=medium)
    water_temp_c = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    water_volume_ml = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(999),
            MinValueValidator(1)
        ]
    )
    brew_time_mins = models.DecimalField(max_digits=4, decimal_places=2)
    products = models.ManyToManyField(Product)
    method = models.TextField()

    def __str__(self):
        return self.name
