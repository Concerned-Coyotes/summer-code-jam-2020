# Generated by Django 3.0.8 on 2020-08-08 17:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_weather_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
