# Generated by Django 5.0.2 on 2024-02-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoardTrip', '0007_delete_cities'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='destination_airport',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='flight',
            name='origin_airport',
            field=models.CharField(default='', max_length=500),
        ),
    ]