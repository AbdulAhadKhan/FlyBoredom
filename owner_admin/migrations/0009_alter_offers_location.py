# Generated by Django 4.1.7 on 2023-03-26 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner_admin', '0008_merge_20230326_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
