# Generated by Django 4.1.3 on 2022-11-13 04:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Residencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residencia', models.CharField(max_length=6)),
                ('Propietario', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='correspondencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name=datetime.date.today)),
                ('recivio', models.CharField(max_length=30)),
                ('estado', models.BooleanField(default=False)),
                ('propietario', models.CharField(max_length=30)),
                ('residencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.residencia')),
            ],
        ),
    ]
