# Generated by Django 4.1.3 on 2022-11-26 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('codigo_pais', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField()),
                ('extra_dec', models.BooleanField(default=False)),
                ('extra_jun', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=15)),
                ('descripcion', models.TextField(null=True)),
                ('salario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.salario')),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('codigo_postal', models.CharField(max_length=5)),
                ('Ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.lugar')),
                ('trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.trabajo')),
            ],
        ),
    ]
