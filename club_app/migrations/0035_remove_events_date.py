# Generated by Django 3.2.8 on 2021-11-21 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0034_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='Date',
        ),
    ]