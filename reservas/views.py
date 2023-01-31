from django.shortcuts import render,redirect
from reservas.models import Disiplina,Instalacion

# Create your views here.
def home(request):
    return render(request, 'home.html')

def instalaciones(request):
    return render(request, 'instalaciones.html')

def detalleInstalacion(request):
    return render(request, 'vista_reserva.html')

def adminDisiplinas(request):
    busqueda= request.GET.get("buscardisiplina")
    listaDisiplinas = Disiplina.objects.all()

    if busqueda:
        listaDisiplinas=Disiplina.objects.filter(
            nombre__icontains=busqueda 
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
    id=request.POST['disiplinaid']
    disiplina = Disiplina.objects.get(id=id)

    if request.POST:
        disiplina=Disiplina()
        disiplina.id = request.POST.get('disiplinaid')
        disiplina.nombre = request.POST.get('disiplinanombre')
        disiplina.save()
    return redirect('/adminDisiplinas')

def eliminacionDisiplina(request,id):
    disiplina=Disiplina.objects.get(id=id)
    disiplina.delete()
    
    return redirect('/adminDisiplinas')    

def adminInstalaciones(request):
    listaDisiplinas = Disiplina.objects.all()
    listaInstalaciones = Instalacion.objects.all()
    busqueda= request.GET.get("buscarinstalacion")

    if busqueda:
        listaInstalaciones=Instalacion.objects.filter(
            nombre__icontains=busqueda 
        ).distinct()

    return render(request, 'adminInstalaciones.html',{'disiplinas': listaDisiplinas,'instalaciones': listaInstalaciones})

def registroInstalacion(request):
    nombre = request.POST['nombre']

    disiplina=Disiplina()
    disiplina.id = int(request.POST['disiplina'])
    disiplina_instalacion=disiplina

    precio = request.POST['precio']
    capacidad = request.POST['capacidad']
    foto = request.FILES['imagen']
    descripcion = request.POST['descripcion']
    indumentaria = request.POST['indumentaria']
    recomendaciones = request.POST['recomendaciones']
    restricciones = request.POST['restricciones']
    equipo_incluido = request.POST['equipo_incluido']
    

    Instalacion.objects.create(
        nombre=nombre,
        id_diciplina=disiplina_instalacion,
        descripcion=descripcion,
        restriciones=restricciones,
        precio=precio,
        capacidad=capacidad,
        imagen=foto,
        indumentaria=indumentaria,
        recomendaciones=recomendaciones,
        equipo_incluido=equipo_incluido,
    )
    return redirect('/adminInstalaciones')


def verInstalacion(request,id):
    verinstalacion = Instalacion.objects.get(id=id)
    listaDisiplinas = Disiplina.objects.all()
    return render(request, 'verInstalaciones.html', {'verInstalacion': verinstalacion,'disiplinas': listaDisiplinas})

def editaInstalacion(request,id):
    edicioninstalacion = Instalacion.objects.get(id=id)
    return render(request, 'edicionInstalaciones.html', {'edicionInstalacion': edicioninstalacion})

def edicionInstalaciones(request):
    return render(request, '/adminInstalaciones')

def eliminacionInstalacion(request,id):
    instalacion=Instalacion.objects.get(id=id)
    instalacion.delete()
    
    return redirect('/adminInstalaciones') 

def adminReservas(request):
    return render(request, 'adminReservas.html')
