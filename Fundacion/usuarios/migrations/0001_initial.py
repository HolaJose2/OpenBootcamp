# Generated by Django 4.1.3 on 2022-11-28 01:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoRol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=15)),
                ('celular', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.CharField(blank=True, max_length=150, null=True)),
                ('fecha_registro', models.DateField(verbose_name=datetime.date.today)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.rol')),
            ],
        ),
    ]
