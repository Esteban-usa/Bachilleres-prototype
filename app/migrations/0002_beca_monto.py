# Generated by Django 4.2.5 on 2023-09-23 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beca',
            name='monto',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
