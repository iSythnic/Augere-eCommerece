# Generated by Django 3.2.7 on 2021-10-04 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bids_categories_comments_listings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='priceOfBid',
            new_name='ammount',
        ),
        migrations.RenameField(
            model_name='bids',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='users',
            new_name='user',
        ),
    ]
