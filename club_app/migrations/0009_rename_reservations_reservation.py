# Generated by Django 3.2.8 on 2021-11-05 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0008_rename_reservstions_reservations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservations',
            new_name='Reservation',
        ),
    ]