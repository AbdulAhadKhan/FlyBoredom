# Generated by Django 4.1.7 on 2023-03-23 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner_admin', '0004_alter_offers_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='spots_available',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
