# Generated by Django 3.2.8 on 2021-11-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0050_feedback_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.CharField(max_length=50),
        ),
    ]
