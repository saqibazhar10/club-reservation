# Generated by Django 3.2.8 on 2021-11-07 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0030_auto_20211107_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registered_user',
            old_name='Membership_End_Time',
            new_name='Membership_End_time',
        ),
    ]