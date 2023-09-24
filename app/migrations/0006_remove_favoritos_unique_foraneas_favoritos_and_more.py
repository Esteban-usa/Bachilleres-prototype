# Generated by Django 4.2.5 on 2023-09-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_union_u_f_unique_foraneas_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='favoritos',
            name='unique_foraneas_favoritos',
        ),
        migrations.AddConstraint(
            model_name='favoritos',
            constraint=models.UniqueConstraint(fields=('usuario', 'Configuracion_Becas', 'tipo'), name='unique_foraneas_favoritos'),
        ),
    ]
