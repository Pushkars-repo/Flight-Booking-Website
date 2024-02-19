# Generated by Django 5.0.2 on 2024-02-19 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoardTrip', '0005_rename_business_fare_flight_fare_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_city', to='BoardTrip.flight')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_city', to='BoardTrip.flight')),
            ],
        ),
        migrations.DeleteModel(
            name='Booked',
        ),
    ]