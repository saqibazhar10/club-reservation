# Generated by Django 3.2.8 on 2021-11-07 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0031_rename_membership_end_time_registered_user_membership_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_user',
            name='Member_Availed',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
