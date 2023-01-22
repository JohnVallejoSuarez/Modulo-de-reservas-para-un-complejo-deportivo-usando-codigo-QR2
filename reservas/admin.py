from django.contrib import admin
from .models import Disiplina, Instalacion, Reserva
# Register your models here.

class DisiplinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'estado')

class InstalacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'restriciones', 'precio', 'capacidad', 'imagen', 'indumentaria', 'recomendaciones', 'equipo_incluido', 'estado')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'cedula', 'email', 'telefono', 'fecha_reservacion', 'fecha_reservada', 'codigo_qr', 'pago', 'hora_inicio', 'hora_fin', 'estado')


admin.site.register(Disiplina, DisiplinaAdmin)
admin.site.register(Instalacion, InstalacionAdmin)
admin.site.register(Reserva, ReservaAdmin)
