from django.shortcuts import render,redirect
from reservas.models import Disiplina

# Create your views here.
def home(request):
    return render(request, 'home.html')

def instalaciones(request):
    return render(request, 'instalaciones.html')

def detalleInstalacion(request):
    return render(request, 'vista_reserva.html')

def adminInstalaciones(request):
    
    return render(request, 'adminInstalaciones.html')

def edicionInstalaciones(request):
    return render(request, 'edicionInstalaciones.html')

def adminDisiplinas(request):
    busqueda= request.GET.get("buscardisiplina")
    listaDisiplinas = Disiplina.objects.all()

    if busqueda:
        listaDisiplinas=Disiplina.objects.filter(
            Q(nombre__icontains=busqueda) 
        ).distinct()
    return render(request, 'adminDisiplinas.html',{'disiplinas': listaDisiplinas})

def registroDisiplina(request):
    nombre = request.POST['disnombre']

    Disiplina.objects.create(
        nombre=nombre,
    )
    return redirect('/adminDisiplinas')

def editaDisiplina(request,id):
    ediciondisiplina = Disiplina.objects.get(id=id)
    return render(request, 'edicionDisiplinas.html', {'edicionDisiplina': ediciondisiplina})

def edicionDisiplinas(request):
    return render(request, 'edicionDisiplinas.html')

def eliminacionDisiplina(request,id):
    disiplina=Disiplina.objects.get(id=id)
    disiplina.delete()
    
    return redirect('/adminDisiplinas')

def adminReservas(request):
    return render(request, 'adminReservas.html')
