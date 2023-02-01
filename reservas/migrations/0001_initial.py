# Generated by Django 4.1.5 on 2023-02-01 04:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disiplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10, unique=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('restriciones', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('capacidad', models.CharField(max_length=10)),
                ('imagen', models.ImageField(upload_to='imagenes/instalaciones/%Y/%m/%d/')),
                ('indumentaria', models.CharField(max_length=200)),
                ('recomendaciones', models.CharField(max_length=200)),
                ('equipo_incluido', models.CharField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
                ('id_diciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.disiplina')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('fecha_reservacion', models.DateField(default=datetime.datetime.now)),
                ('fecha_reservada', models.DateField()),
                ('codigo_qr', models.CharField(max_length=255, unique=True)),
                ('pago', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('hora_inicio', models.IntegerField(choices=[[0, '08:00:00'], [1, '09:00:00'], [2, '10:00:00'], [3, '11:00:00'], [4, '12:00:00'], [5, '13:00:00'], [6, '14:00:00'], [7, '15:00:00'], [8, '16:00:00'], [9, '17:00:00'], [10, '18:00:00'], [11, '19:00:00'], [12, '20:00:00'], [13, '21:00:00']])),
                ('hora_fin', models.IntegerField(choices=[[0, '09:00:00'], [1, '10:00:00'], [2, '11:00:00'], [3, '12:00:00'], [4, '13:00:00'], [5, '14:00:00'], [6, '15:00:00'], [7, '16:00:00'], [8, '17:00:00'], [9, '18:00:00'], [10, '19:00:00'], [11, '20:00:00'], [12, '21:00:00'], [13, '22:00:00']])),
                ('estado', models.BooleanField(default=True)),
                ('id_instalacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.instalacion')),
            ],
        ),
    ]
