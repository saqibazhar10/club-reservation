# Generated by Django 3.2.8 on 2021-11-21 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0035_remove_events_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='Date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]