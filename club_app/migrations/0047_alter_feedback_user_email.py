# Generated by Django 3.2.8 on 2021-11-27 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0046_auto_20211128_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user_email',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
