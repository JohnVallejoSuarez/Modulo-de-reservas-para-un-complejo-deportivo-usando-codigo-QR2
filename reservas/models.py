from django.db import models
from datetime import datetime #tiempo
# Create your models here.

class Disiplina(models.Model):
    nombre = models.CharField(max_length=10, unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Instalacion(models.Model):
    id_diciplina = models.ForeignKey(Disiplina, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=200)
    restriciones = models.CharField(max_length=200)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    capacidad = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='imagenes/instalaciones/%Y/%m/%d/')
    indumentaria = models.CharField(max_length=200)
    recomendaciones = models.CharField(max_length=200)
    equipo_incluido = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


opciones_horaInicio = [
    [0,'08:00:00'],
    [1,'09:00:00'],
    [2,'10:00:00'],
    [3,'11:00:00'],
    [4,'12:00:00'],
    [5,'13:00:00'],
    [6,'14:00:00'],
    [7,'15:00:00'],
    [8,'16:00:00'],
    [9,'17:00:00'],
    [10,'18:00:00'],
    [11,'19:00:00'],
    [12,'20:00:00'],
    [13,'21:00:00'],
]

opciones_horaFin = [
    [0,'09:00:00'],
    [1,'10:00:00'],
    [2,'11:00:00'],
    [3,'12:00:00'],
    [4,'13:00:00'],
    [5,'14:00:00'],
    [6,'15:00:00'],
    [7,'16:00:00'],
    [8,'17:00:00'],
    [9,'18:00:00'],
    [10,'19:00:00'],
    [11,'20:00:00'],
    [12,'21:00:00'],
    [13,'22:00:00'],
]

class Reserva(models.Model):
    id_instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    fecha_reservacion = models.DateField(default=datetime.now)
    fecha_reservada = models.DateField()
    codigo_qr = models.CharField(max_length=255, unique=True)
    pago = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    hora_inicio = models.IntegerField(choices=opciones_horaInicio)
    hora_fin = models.IntegerField(choices=opciones_horaFin)
    estado = models.BooleanField(default=True)