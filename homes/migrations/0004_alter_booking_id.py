# Generated by Django 5.0.6 on 2024-09-19 12:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0003_listingimage_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
