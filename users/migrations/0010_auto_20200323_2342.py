# Generated by Django 3.0.4 on 2020-03-23 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_poule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='origin_profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='psn_profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='xboxlive_profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='profile',
            name='identifiant',
            field=models.CharField(default='none provided', max_length=150, verbose_name='Identifiant'),
        ),
        migrations.AddField(
            model_name='profile',
            name='platform',
            field=models.CharField(choices=[('a', 'PS4'), ('b', 'XBOX')], default='a', max_length=1, verbose_name='Platforme du joueur'),
        ),
    ]
