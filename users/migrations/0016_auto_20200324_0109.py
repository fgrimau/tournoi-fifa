# Generated by Django 3.0.4 on 2020-03-24 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='tournoi_fifa/assets/img/avatars/', verbose_name='profile picture'),
        ),
    ]
