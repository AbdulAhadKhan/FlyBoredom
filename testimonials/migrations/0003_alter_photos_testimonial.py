# Generated by Django 3.2.18 on 2023-03-12 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_remove_testimonial_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='testimonial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='testimonials.testimonial'),
        ),
    ]
