# Generated by Django 3.2.8 on 2021-11-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0037_registered_user_applied_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Court_Id',
            field=models.IntegerField(max_length=10),
        ),
    ]