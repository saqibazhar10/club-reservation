# Generated by Django 3.2.8 on 2021-11-27 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0045_feedback_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='suggestion',
            new_name='commentText',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='Experience',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='rank',
            new_name='rating1',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='star_2',
            new_name='rating2',
        ),
    ]
