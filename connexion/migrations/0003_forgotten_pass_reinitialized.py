# Generated by Django 3.0.4 on 2020-03-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connexion', '0002_auto_20200324_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='forgotten_pass',
            name='reinitialized',
            field=models.BooleanField(default=False),
        ),
    ]