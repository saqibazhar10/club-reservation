# Generated by Django 3.2.8 on 2021-11-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0023_reservation_court_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered_user',
            name='Member_Availed',
            field=models.CharField(choices=[('none', 'None'), ('basic', 'Basic'), ('standard', 'Standard'), ('premiun', 'Premium')], default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='registered_user',
            name='User_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
