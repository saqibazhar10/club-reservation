# Generated by Django 3.2.8 on 2021-12-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0060_auto_20211202_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='Reservation_Id',
        ),
        migrations.AddField(
            model_name='reservation',
            name='id',
            field=models.BigAutoField(auto_created=True, default=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
