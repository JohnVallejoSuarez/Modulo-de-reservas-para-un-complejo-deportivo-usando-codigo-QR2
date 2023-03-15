from django.shortcuts import render,redirect
from reservas.models import Disiplina,Instalacion, Reserva,Horario

from django.http import JsonResponse

from django.contrib.auth.views import LoginView,LogoutView
import complejo.settings as setting


from django.db.models import Q

import qrcode
from io import BytesIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from django.template.loader import render_to_string
from datetime import datetime

from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.views.generic import TemplateView

from django.db.models import FloatField



import base64
# Create your views here.
def home(request):
    return render(request, 'home.html')

class LoginFormView(LoginView):
    template_name ='home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['title']="Iniciar Secion"
        return context
    
# def adminInicio(request):
#     return render(request, 'adminInicio.html')

class adminInicioView(TemplateView):
    template_name = 'adminInicio.html'

    def get_graph_sales_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                total = Reserva.objects.filter(fecha_reservacion__year=year, fecha_reservacion__month=m).aggregate(r=Coalesce(Sum('pago'), 0,output_field=FloatField())).get('r')
                data.append(float(total))
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['graph_sales_year_month'] = self.get_graph_sales_year_month()
        return context

def instalaciones(request):
    listaInstalaciones = Instalacion.objects.all()
    return render(request, 'instalaciones.html',{'instalaciones': listaInstalaciones})
    

def detalleInstalacion(request,id):
    verinstalacion = Instalacion.objects.get(id=id)
    listaDisiplinas = Disiplina.objects.all()
    listaReservas=Reserva.objects.all()
    listaHorarios = Horario.objects.all()

    data = {
        'horarios':listaHorarios,
        'verInstalacion':verinstalacion,
        'disiplinas': listaDisiplinas,
        'reservass':listaReservas, 
    }

    return render(request, 'vista_reserva.html',data)


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
    listaReservas=Reserva.objects.all()
    listaHorarios = Horario.objects.all()
   
    data = {'verInstalacion':verinstalacion,'disiplinas': listaDisiplinas,'reservas':listaReservas,'horarios':listaHorarios,}
    
    return render(request, 'verInstalaciones.html',  data)

def editaInstalacion(request,id):
    edicioninstalacion = Instalacion.objects.get(id=id)
    imagen=edicioninstalacion.imagen
    if request.POST:
        if request.POST.get('imagen')=='':
            instalacion=Instalacion()
            instalacion.id = edicioninstalacion.id
            instalacion.nombre=request.POST.get('nombre')
            
            disiplina=Disiplina()
            disiplina.id=request.POST.get('disiplina')
            instalacion.id_diciplina=disiplina

            instalacion.precio=request.POST.get('precio')
            instalacion.capacidad=request.POST.get('capacidad')
            instalacion.imagen=imagen
            instalacion.descripcion=request.POST.get('descripcion')
            instalacion.indumentaria=request.POST.get('indumentaria')
            instalacion.recomendaciones=request.POST.get('recomendaciones')
            instalacion.restriciones=request.POST.get('restricciones')
            instalacion.equipo_incluido=request.POST.get('equipo_incluido')

            instalacion.save()
        else:
            instalacion=Instalacion()
            instalacion.id = edicioninstalacion.id
            instalacion.nombre=request.POST.get('nombre')
            
            disiplina=Disiplina()
            disiplina.id=request.POST.get('disiplina')
            instalacion.id_diciplina=disiplina

            instalacion.precio=request.POST.get('precio')
            instalacion.capacidad=request.POST.get('capacidad')
            instalacion.imagen=request.FILES.get('imagen')
            instalacion.descripcion=request.POST.get('descripcion')
            instalacion.indumentaria=request.POST.get('indumentaria')
            instalacion.recomendaciones=request.POST.get('recomendaciones')
            instalacion.restriciones=request.POST.get('restricciones')
            instalacion.equipo_incluido=request.POST.get('equipo_incluido')

            instalacion.save()

    return redirect('/verInstalacion/'+str(instalacion.id))

def eliminacionInstalacion(request,id):
    instalacion=Instalacion.objects.get(id=id)
    instalacion.delete()
    
    return redirect('/adminInstalaciones') 

def adminReservas(request):
    listaReserva = Reserva.objects.all()
    # horariosReservados=listaReserva.horario.all()
    busqueda= request.GET.get("buscarreserva")

    
    reservas = Reserva.objects.select_related('id_instalacion').prefetch_related('horario').all()
    if busqueda:
        reservas=Reserva.objects.filter(
            Q(cedula__icontains=busqueda) |
            Q(nombres__icontains=busqueda) |
            Q(apellidos__icontains=busqueda)|
            Q(fecha_reservacion__icontains=busqueda) |
            Q(fecha_reservada__icontains=busqueda)|
            Q(id_instalacion__nombre__icontains=busqueda)  #Para buscar en un foraneo

        ).distinct()
    data = {'reservas':reservas}
    return render(request, 'adminReservas.html', data)

def registroReservas(request,id):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    ci = request.POST['ci']
    telefono = request.POST['telefono']
    correo = request.POST['correo']

    instalacion=Instalacion()
    instalacion.id = int(id)
    instalacion_reserva=instalacion

    pago = request.POST['pago']
    fecha_reserva = request.POST['fecha_reserva']
    horario = request.POST.getlist('horario')
    reserva = Reserva.objects.create(
        nombres=nombre,
        apellidos=apellido,
        cedula=ci,
        telefono=telefono,
        email=correo,
        id_instalacion=instalacion_reserva,
        fecha_reservada=fecha_reserva,
        pago=pago,  
    )

    reserva.horario.set(horario)

     # Nombre y apellidos 
    nombre = f"{reserva.nombres} {reserva.apellidos}"
    # Actualizar el código QR con el ID de la reserva
    codigo_qr_data = f"{reserva.id},{fecha_reserva},{', '.join(str(h) for h in reserva.horario.all())},{nombre},{correo}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(codigo_qr_data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image_buffer = BytesIO()
    qr_image.save(qr_image_buffer, format="PNG")
    qr_image_data = qr_image_buffer.getvalue()

    # Guardar el código QR actualizado en la reserva y guardar la reserva en la base de datos
    reserva.codigo_qr = codigo_qr_data
    reserva.save()

    # Obtener el objeto Instalacion correspondiente a la reserva
    instalacion_reserva = reserva.id_instalacion

    # Crear una cadena de texto con la información adicional

    horarios = f"{', '.join(str(h) for h in reserva.horario.all())}"
    instalacion = instalacion_reserva.nombre
    fecha_reserva = reserva.fecha_reservada
    data = {
        'horarios':horarios,
        'nombre':nombre,
        'instalacion':instalacion,
        'fecha_reserva':fecha_reserva,
    }
    email_body = render_to_string('correo_reserva.html', data)

    # Enviar el correo electrónico
    send_email(
        email_from='correo',
        email_to=correo,
        email_subject=f'Código QR para la reserva en la instalación {instalacion}',
        email_body=email_body,
        qr_image_data=qr_image_data
    )
    return redirect('/adminReservas')

def send_email(email_from, email_to, email_subject, email_body, qr_image_data):
    # Configurar el servidor SMTP
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(email_from, 'contraseña')

    # Crear el mensaje de correo electrónico
    message = MIMEMultipart()
    message['Subject'] = email_subject
    message['From'] = email_from
    message['To'] = email_to

    # Agregar el cuerpo del correo electrónico como HTML
    html_body = MIMEText(email_body, 'html')
    message.attach(html_body)

    # Agregar la imagen del código QR como un adjunto
    qr_image_attachment = MIMEImage(qr_image_data)
    qr_image_attachment.add_header('Content-ID', '<qr_image>')
    qr_image_attachment.add_header('Content-Disposition', 'inline', filename='qr.png')
    message.attach(qr_image_attachment)

    # Enviar el correo electrónico
    smtp_server.sendmail(email_from, email_to, message.as_string())

    # Cerrar la conexión con el servidor SMTP
    smtp_server.quit()

def registroReservasU(request, id):
    # Obtener los datos de la reserva del formulario
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    ci = request.POST['ci']
    telefono = request.POST['telefono']
    correo = request.POST['correo']
    pago = request.POST['pago']
    fecha_reserva = request.POST['fecha_reserva']
    horarios = request.POST.getlist('horario')

    # Crear un objeto Instalacion para asignar a la reserva
    instalacion = Instalacion.objects.get(id=id)

    # Crear y guardar la reserva en la base de datos
    reserva = Reserva.objects.create(
        nombres=nombre,
        apellidos=apellido,
        cedula=ci,
        telefono=telefono,
        email=correo,
        id_instalacion=instalacion,
        fecha_reservada=fecha_reserva,
        pago=pago,
    )
    reserva.horario.set(horarios)
    
    # Nombre y apellidos 
    nombre = f"{reserva.nombres} {reserva.apellidos}"
    # Actualizar el código QR con el ID de la reserva
    # codigo_qr_data = f"{reserva.id},{fecha_reserva},{', '.join(str(h) for h in reserva.horario.all())},{nombre},{correo}"
    codificado = base64.b64encode(str(reserva.id).encode('utf-8'))
    # codigo_qr_data = f'Reserva de: {reserva.nombres} {reserva.apellidos} con el número #{codificado}'
    # codigo_qr_data = f'Reserva #{codificado}'

    #codigo_qr_data = reserva.id
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(f'Reserva: {codificado}')
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image_buffer = BytesIO()
    qr_image.save(qr_image_buffer, format="PNG")
    qr_image_data = qr_image_buffer.getvalue()

    # Guardar el código QR actualizado en la reserva y guardar la reserva en la base de datos
    reserva.codigo_qr = codificado
    reserva.save()

    # Obtener el objeto Instalacion correspondiente a la reserva
    instalacion_reserva = reserva.id_instalacion

    # Crear una cadena de texto con la información adicional

    horarios = f"{', '.join(str(h) for h in reserva.horario.all())}"
    instalacion = instalacion_reserva.nombre
    fecha_reserva = reserva.fecha_reservada
    data = {
        'horarios':horarios,
        'nombre':nombre,
        'instalacion':instalacion,
        'fecha_reserva':fecha_reserva,
    }
    email_body = render_to_string('correo_reserva.html', data)

    # Enviar el correo electrónico
    send_email(
        email_from='correo',
        email_to=correo,
        email_subject=f'Código QR para la reserva en la instalación {instalacion}',
        email_body=email_body,
        qr_image_data=qr_image_data
    )

    return redirect('/instalaciones')

#---Pago Hecho desde el Cliente
def pagoonline(request,id):

    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    ci = request.POST['ci']
    telefono = request.POST['telefono']
    correo = request.POST['correo']
    instalacion=Instalacion()
    instalacion.id = int(id)
    instalacion_reserva=instalacion
    
    pago = request.POST['pago']
    fecha_reserva = request.POST['fecha_reserva']
    horario = request.POST.getlist('horario')

    reserva = Reserva.objects.create(
        nombres=nombre,
        apellidos=apellido,
        cedula=ci,
        telefono=telefono,
        email=correo,
        id_instalacion=instalacion_reserva,
        
    )

    reserva.horario.set(horario)

    codificado = base64.b64encode(str(reserva.id).encode('utf-8'))
    # codigo_qr_data = f'Reserva de: {reserva.nombres} {reserva.apellidos} con el número #{codificado}'
    # codigo_qr_data = f'Reserva #{codificado}'

    #codigo_qr_data = reserva.id
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(f'Reserva: {codificado}')
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image_buffer = BytesIO()
    qr_image.save(qr_image_buffer, format="PNG")
    qr_image_data = qr_image_buffer.getvalue()

    # Guardar el código QR actualizado en la reserva y guardar la reserva en la base de datos
    reserva.codigo_qr = codificado
    reserva.save()
    
  

    data = {'nombres':nombre,'apellidos': apellido,'ci':ci,'telefonos':telefono,'correos':correo,'instalaciones': instalacion_reserva,'codigos':codificado,'pagos':pago,'fecha_reservas':fecha_reserva,'horarios':horario}
    return render(request, 'pago.html', data)
   
    
# def regpago(request,nombres,apellidos,ci,telefonos,correos,instalaciones,codigos,pagos,fecha_reservas,horarios):

#     reserva = Reserva.objects.create(
#         nombres=nombres,
#         apellidos=apellidos,
#         cedula=ci,
#         telefono=telefonos,
#         email=correos,
#         id_instalacion=instalaciones,
#         fecha_reservada=fecha_reservas,
#         codigo_qr=codigos,
#         pago=pagos,  
#     )

#     reserva.horario.set(horarios)
#     return redirect('/instalaciones')

def regpago(request):
    reservas=Reserva.objects.all().last()

    
    pagos = request.GET.get('pagos')
    fecha_reservas = request.GET.get('fecha_reservas')
    

    reserva=Reserva.objects.get(id=reservas.id)
    reserva.fecha_reservada=fecha_reservas
    reserva.pago=pagos
    reserva.save()

    # Nombre y apellidos 
    nombre = f"{reserva.nombres} {reserva.apellidos}"
    # Actualizar el código QR con el ID de la reserva
    # codigo_qr_data = f"{reserva.id},{fecha_reserva},{', '.join(str(h) for h in reserva.horario.all())},{nombre},{correo}"
    
    # codigo_qr_data = f'Reserva de: {reserva.nombres} {reserva.apellidos} con el número #{codificado}'
    # codigo_qr_data = f'Reserva #{codificado}'

    #codigo_qr_data = reserva.id
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(f'Reserva: {reserva.codigo_qr}')
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image_buffer = BytesIO()
    qr_image.save(qr_image_buffer, format="PNG")
    qr_image_data = qr_image_buffer.getvalue()



    # Obtener el objeto Instalacion correspondiente a la reserva
    instalacion_reserva = reserva.id_instalacion

    # Crear una cadena de texto con la información adicional

    horarios = f"{', '.join(str(h) for h in reserva.horario.all())}"
    instalacion = instalacion_reserva.nombre
    fecha_reserva = reserva.fecha_reservada
    data = {
        'horarios':horarios,
        'nombre':nombre,
        'instalacion':instalacion,
        'fecha_reserva':fecha_reserva,
    }
    email_body = render_to_string('correo_reserva.html', data)

    # Enviar el correo electrónico
    send_email(
        email_from='correo',
        email_to=reserva.email,
        email_subject=f'Código QR para la reserva en la instalación {instalacion}',
        email_body=email_body,
        qr_image_data=qr_image_data
    )


    return redirect('/instalaciones')

def eliminacionReserva(request,id):
    reserva=Reserva.objects.get(id=id)
    reserva.delete()
    
    return redirect('/adminReservas') 

# def regpago(request):

#     nombres = request.GET.get('nombres')
#     apellidos = request.GET.get('apellidos')
#     ci = request.GET.get('ci')
#     telefonos = request.GET.get('telefonos')
#     correos = request.GET.get('correos')
#     instalacion=Instalacion()
#     instalacion.id = int(request.GET.get('instalaciones'))
#     instalacion_reserva=instalacion


#     codigos= request.GET.get('codigos')
#     pagos = request.GET.get('pagos')
#     fecha_reservas = request.GET.get('fecha_reservas')
#     horarios = request.GET.getlist('horarios')

#     reserva = Reserva.objects.create(
#         nombres=nombres,
#         apellidos=apellidos,
#         cedula=ci,
#         telefono=telefonos,
#         email=correos,
#         id_instalacion=instalacion_reserva,
#         fecha_reservada=fecha_reservas,
#         codigo_qr=codigos,
#         pago=pagos,  
#     )

#     reserva.horario.set(horarios)
#     return redirect('/instalaciones')


#-------Horarios
def adminHorarios(request):
    busqueda= request.GET.get("buscarhorario")
    listaHorarios = Horario.objects.all()

    if busqueda:
        listaHorarios=Horario.objects.filter(
            nombre__icontains=busqueda 
        ).distinct()
    return render(request, 'adminHorarios.html',{'horarios': listaHorarios})

def registroHorario(request):
    horarioInicio = request.POST['horaInicio']
    horarioFinal = request.POST['horaFinal']
    

    Horario.objects.create(
        HorarioInicio=horarioInicio,
        HorarioFin=horarioFinal,
    )
    return redirect('/adminHorarios')

# def editaDisiplina(request,id):
#     ediciondisiplina = Disiplina.objects.get(id=id)
#     return render(request, 'edicionDisiplinas.html', {'edicionDisiplina': ediciondisiplina})

# def edicionDisiplinas(request):
#     id=request.POST['disiplinaid']
#     disiplina = Disiplina.objects.get(id=id)

#     if request.POST:
#         disiplina=Disiplina()
#         disiplina.id = request.POST.get('disiplinaid')
#         disiplina.nombre = request.POST.get('disiplinanombre')
#         disiplina.save()
#     return redirect('/adminDisiplinas')

def eliminacionHorario(request,id):
    horario=Horario.objects.get(id=id)
    horario.delete()
    
    return redirect('/adminHorarios')    
# def regpago(data):

#     reserva = Reserva.objects.create(
#         nombres=data.nombres,
#         apellidos=data.apellidos,
#         cedula=data.ci,
#         telefono=data.telefonos,
#         email=data.correos,
#         id_instalacion=data.instalaciones,
#         fecha_reservada=data.fecha_reservas,
#         codigo_qr=data.codigos,
#         pago=data.pagos,  
#     )

#     reserva.horario.set(data.horarios)
#     return redirect('/instalaciones')

def reservas_api(request):
    id_instalacion = request.GET.get('id_instalacion')
    fecha_reservada = request.GET.get('fecha_reservada')
    
    # Obtener la instalación correspondiente al id dado
    instalacion = Instalacion.objects.get(id=id_instalacion)
    
    # Obtener los horarios reservados para la fecha dada y la instalación
    reservas = Reserva.objects.filter(id_instalacion_id=id_instalacion, fecha_reservada=fecha_reservada)

    horarios_reservados = []
    for reserva in reservas:
        horarios_reservados.extend(reserva.horario.all())

    # Obtener todos los horarios disponibles para la instalación
    horarios_instalacion = Horario.objects.all()
    horarios_disponibles = [horario for horario in horarios_instalacion if horario not in horarios_reservados]

    # Serializar los horarios disponibles y retornarlos en formato JSON
    horarios_disponibles_serializados = [{'id': horario.id, 'HorarioInicio': horario.HorarioInicio, 'HorarioFin': horario.HorarioFin} for horario in horarios_disponibles]
    return JsonResponse(horarios_disponibles_serializados, safe=False)


def validarFecha(request):
    fecha = request.GET.get('fecha_reserva', None)
    data = {
        'is_taken': Reserva.objects.filter(fecha_reservada=fecha).exists()
    }
    
    return JsonResponse(data)


def scaner(request):
    return render(request, 'adminScanner.html')

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Reserva


from django.core.serializers import serialize
from django.http import JsonResponse
@ensure_csrf_cookie
def actualizar_estado(request):
    if request.method == 'POST':
        qr_value = request.POST.get('qr_value')
        valor = qr_value.split(':')[1].strip()
        reserva = Reserva.objects.filter(codigo_qr=valor).first()
        if reserva:
            reserva.estado2 = True
            reserva.save()
            reserva_json = serialize('json', [reserva])
            return JsonResponse({'success': True, 'reserva': reserva_json})
        else:
            return JsonResponse({'success': False, 'error_message': 'No se encontró una reserva con este código QR.'})