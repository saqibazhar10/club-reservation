# Generated by Django 3.2.8 on 2021-11-06 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0019_alter_reservation_court_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
