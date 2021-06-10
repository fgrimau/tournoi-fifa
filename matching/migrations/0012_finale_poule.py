# Generated by Django 3.0.4 on 2020-04-02 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matching', '0011_auto_20200331_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finale_poule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0)),
                ('finished', models.BooleanField(default=False)),
                ('winner', models.IntegerField(default=0, verbose_name='winner nb')),
                ('platform', models.CharField(choices=[('ps4', 'PS4'), ('xbox', 'XBOX')], default='ps4', max_length=4, verbose_name='platforme')),
                ('player1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='as_finale_player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='as_finale_player2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]