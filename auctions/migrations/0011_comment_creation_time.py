# Generated by Django 4.1.2 on 2022-10-25 02:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_listing_creation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
