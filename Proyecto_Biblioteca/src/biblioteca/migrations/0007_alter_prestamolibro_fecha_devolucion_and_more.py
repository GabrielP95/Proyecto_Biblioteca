# Generated by Django 4.2.1 on 2023-05-21 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_prestamolibro_empleado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamolibro',
            name='fecha_devolucion',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 21, 16, 46, 36, 153588)),
        ),
        migrations.AlterField(
            model_name='prestamolibro',
            name='fecha_prestamos',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 21, 16, 46, 36, 153588)),
        ),
    ]
