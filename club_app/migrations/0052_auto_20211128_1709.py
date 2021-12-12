# Generated by Django 3.2.8 on 2021-11-28 12:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0051_alter_feedback_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='Time',
            new_name='End_Time',
        ),
        migrations.AddField(
            model_name='reservation',
            name='Reserved_person',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='reservation',
            name='Start_Time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]