# Generated by Django 2.2.6 on 2020-02-15 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0003_brand_car_fleet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='fleet',
            name='car',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Fleet',
        ),
    ]
