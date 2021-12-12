# Generated by Django 3.2.8 on 2021-11-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0018_alter_reservation_court_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Court_Person',
            field=models.CharField(choices=[('S', 'Single'), ('D', 'Double')], default=True, max_length=1),
            preserve_default=False,
        ),
    ]
