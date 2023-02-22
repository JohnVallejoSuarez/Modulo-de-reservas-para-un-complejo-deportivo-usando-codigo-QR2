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

class Horario(models.Model):
    HorarioInicio = models.TimeField(blank=True)
    HorarioFin = models.TimeField(blank=True)

    def __str__(self):
        return f'{self.HorarioInicio} - {self.HorarioFin}'


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
    horario = models.ManyToManyField(Horario)
    estado = models.BooleanField(default=True)
