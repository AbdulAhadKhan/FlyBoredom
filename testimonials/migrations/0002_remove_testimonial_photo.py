# Generated by Django 3.2.18 on 2023-03-12 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='photo',
        ),
    ]
