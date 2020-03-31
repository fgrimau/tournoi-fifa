# Generated by Django 3.0.4 on 2020-03-31 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0007_history_played'),
        ('users', '0018_auto_20200331_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='poule',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pool_players', to='matching.Poule'),
        ),
    ]
