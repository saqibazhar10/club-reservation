# Generated by Django 3.2.8 on 2021-11-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0025_auto_20211107_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_user',
            name='Membership_End_Time',
            field=models.DateField(default='False'),
        ),
        migrations.AlterField(
            model_name='registered_user',
            name='Membership_Start_time',
            field=models.DateField(default='False'),
        ),
    ]
