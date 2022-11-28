# Generated by Django 4.1.3 on 2022-11-27 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=12, null=True)),
                ('celular', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('compañia', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_registro', models.DateField(default=datetime.date.today)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
