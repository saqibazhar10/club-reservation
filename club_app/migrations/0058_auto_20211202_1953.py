# Generated by Django 3.2.8 on 2021-12-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0057_auto_20211202_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_user',
            name='Membership_End_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='registered_user',
            name='Membership_Start_time',
            field=models.DateField(),
        ),
    ]
