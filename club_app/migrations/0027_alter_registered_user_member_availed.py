# Generated by Django 3.2.8 on 2021-11-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0026_auto_20211107_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_user',
            name='Member_Availed',
            field=models.CharField(max_length=50),
        ),
    ]
