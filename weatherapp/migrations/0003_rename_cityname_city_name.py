# Generated by Django 4.0.5 on 2022-06-08 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0002_rename_name_city_cityname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='cityName',
            new_name='name',
        ),
    ]
