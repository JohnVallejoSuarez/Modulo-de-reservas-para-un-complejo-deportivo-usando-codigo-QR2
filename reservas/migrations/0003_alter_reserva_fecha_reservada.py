# Generated by Django 4.1.5 on 2023-03-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_reserva_estado2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_reservada',
            field=models.DateField(default=' '),
        ),
    ]
