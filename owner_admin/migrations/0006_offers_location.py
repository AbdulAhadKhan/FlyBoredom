# Generated by Django 4.1.7 on 2023-03-25 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner_admin', '0005_offers_spots_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='location',
            field=models.TextField(blank=True),
        ),
    ]