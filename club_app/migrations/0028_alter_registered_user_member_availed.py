# Generated by Django 3.2.8 on 2021-11-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0027_alter_registered_user_member_availed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_user',
            name='Member_Availed',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
