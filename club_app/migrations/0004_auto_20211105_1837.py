# Generated by Django 3.2.8 on 2021-11-05 13:37

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0003_rename_users_registered_user'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='registered_user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='registered_user',
            name='product_name',
        ),
    ]
