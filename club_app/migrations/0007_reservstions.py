# Generated by Django 3.2.8 on 2021-11-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0006_alter_registered_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservstions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Court_Type', models.CharField(max_length=50)),
                ('Court_Person', models.CharField(choices=[('S', 'Single'), ('D', 'Double')], max_length=1)),
                ('Club_Id', models.IntegerField(unique=True)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
            ],
        ),
    ]
