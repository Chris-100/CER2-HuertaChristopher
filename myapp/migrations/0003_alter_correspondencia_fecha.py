# Generated by Django 4.1.3 on 2022-11-13 04:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_estado_correspondencia_entregado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]