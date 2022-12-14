# Generated by Django 4.1.3 on 2022-11-28 02:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_rename_fecha_usuario_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_registro',
            field=models.DateField(null=True, verbose_name=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.rol'),
        ),
    ]
