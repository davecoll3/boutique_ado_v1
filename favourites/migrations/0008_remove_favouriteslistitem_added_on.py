# Generated by Django 3.2.18 on 2023-05-14 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0007_auto_20230514_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favouriteslistitem',
            name='added_on',
        ),
    ]
