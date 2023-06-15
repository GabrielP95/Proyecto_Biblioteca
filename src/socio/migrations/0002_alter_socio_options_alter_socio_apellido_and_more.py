# Generated by Django 4.2.1 on 2023-05-30 01:01

from django.db import migrations, models
import socio.validators


class Migration(migrations.Migration):

    dependencies = [
        ('socio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socio',
            options={'ordering': ['apellido', 'nombre', 'fecha_nacimiento']},
        ),
        migrations.AlterField(
            model_name='socio',
            name='apellido',
            field=models.CharField(max_length=30, validators=[socio.validators.nombreValidator]),
        ),
        migrations.AlterField(
            model_name='socio',
            name='nombre',
            field=models.CharField(max_length=30, validators=[socio.validators.nombreValidator]),
        ),
    ]