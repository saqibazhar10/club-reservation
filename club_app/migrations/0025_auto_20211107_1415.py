# Generated by Django 3.2.8 on 2021-11-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0024_auto_20211106_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered_user',
            name='Membership_End_Time',
            field=models.CharField(default=False, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registered_user',
            name='Membership_Start_time',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
    ]
