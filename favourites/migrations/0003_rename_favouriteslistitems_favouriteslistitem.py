# Generated by Django 3.2.18 on 2023-05-14 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230404_1033'),
        ('favourites', '0002_auto_20230514_1125'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavouritesListItems',
            new_name='FavouritesListItem',
        ),
    ]