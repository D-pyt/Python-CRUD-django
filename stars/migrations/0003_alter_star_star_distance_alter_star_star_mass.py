# Generated by Django 4.2.5 on 2023-09-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0002_star_delete_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='star_distance',
            field=models.TextField(max_length=25),
        ),
        migrations.AlterField(
            model_name='star',
            name='star_mass',
            field=models.TextField(max_length=25),
        ),
    ]
