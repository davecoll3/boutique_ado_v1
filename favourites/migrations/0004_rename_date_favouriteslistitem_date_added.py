# Generated by Django 3.2.18 on 2023-05-14 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0003_rename_favouriteslistitems_favouriteslistitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favouriteslistitem',
            old_name='date',
            new_name='date_added',
        ),
    ]