# Generated by Django 3.2.18 on 2023-05-14 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230404_1033'),
        ('profiles', '0001_initial'),
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouriteslist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_user', to='profiles.userprofile'),
        ),
        migrations.CreateModel(
            name='FavouritesListItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('favourites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_list', to='favourites.favouriteslist')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_products', to='products.product')),
            ],
        ),
    ]
