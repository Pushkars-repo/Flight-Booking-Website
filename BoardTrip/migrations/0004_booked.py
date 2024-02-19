# Generated by Django 5.0.2 on 2024-02-18 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoardTrip', '0003_remove_flight_duration_flight_airline_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_location', to='BoardTrip.flight')),
                ('to_destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_destination', to='BoardTrip.flight')),
            ],
        ),
    ]
