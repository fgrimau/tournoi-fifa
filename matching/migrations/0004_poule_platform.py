# Generated by Django 3.0.4 on 2020-03-21 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0003_history_poule'),
    ]

    operations = [
        migrations.AddField(
            model_name='poule',
            name='platform',
            field=models.CharField(choices=[('a', 'PS4'), ('b', 'XBOX')], default='a', max_length=1, verbose_name='platforme'),
        ),
    ]
