# Generated by Django 3.0.4 on 2020-03-31 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0008_auto_20200331_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='looser_points',
            new_name='player1_points',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='winner_points',
            new_name='player2_points',
        ),
    ]