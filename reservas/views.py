from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def instalaciones(request):
    return render(request, 'instalaciones.html')

def detalleInstalacion(request):
    return render(request, 'vista_reserva.html')