# Generated by Django 5.0.1 on 2024-02-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='sw',
            name='Vehicles',
            field=models.ManyToManyField(to='main_app.vehicle'),
        ),
    ]
