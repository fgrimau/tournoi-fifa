# Generated by Django 3.0.4 on 2020-03-31 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0010_auto_20200331_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date_played',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
