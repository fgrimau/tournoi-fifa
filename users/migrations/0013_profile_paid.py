# Generated by Django 3.0.4 on 2020-03-23 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200324_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
