# Generated by Django 4.1.3 on 2022-11-27 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('shot_description', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('stock', models.IntegerField(default=20)),
            ],
        ),
    ]
