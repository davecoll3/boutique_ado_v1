# Generated by Django 3.2.18 on 2023-05-14 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0004_rename_date_favouriteslistitem_date_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favouriteslistitem',
            old_name='date_added',
            new_name='added_on',
        ),
    ]