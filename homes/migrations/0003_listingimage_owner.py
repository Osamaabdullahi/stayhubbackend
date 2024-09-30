# Generated by Django 5.0.6 on 2024-09-19 06:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0002_listing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingimage',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_images', to=settings.AUTH_USER_MODEL),
        ),
    ]
