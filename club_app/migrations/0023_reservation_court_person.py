# Generated by Django 3.2.8 on 2021-11-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0022_remove_reservation_court_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='Court_Person',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
    ]
