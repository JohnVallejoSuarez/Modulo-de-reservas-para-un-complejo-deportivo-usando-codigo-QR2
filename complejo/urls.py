"""complejo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from reservas import views
from reservas.views import LoginFormView,LogoutView,adminInicioView
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    path('', LoginFormView.as_view(),name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),

    path('adminInicio/',login_required(adminInicioView.as_view()), name='adminInicio'),

    path('instalaciones/', views.instalaciones, name='instalaciones'),
    path('detalleInstalacion/<id>', views.detalleInstalacion, name='detalleInstalacion'),
    

    path('adminDisiplinas/', login_required(views.adminDisiplinas), name='adminDisiplinas'),
    path('registroDisiplina/', login_required(views.registroDisiplina), name='registroDisiplina'), 
    path('edicionDisiplinas/', login_required(views.edicionDisiplinas), name='edicionDisiplinas'),
    path('editaDisiplina/<id>', login_required(views.editaDisiplina), name='editaDisiplina'),
    path('eliminacionDisiplina/<id>', login_required(views.eliminacionDisiplina), name='eliminacionDisiplina'),
     

    path('adminInstalaciones/', login_required(views.adminInstalaciones), name='adminInstalaciones'),
    path('registroInstalacion/', login_required(views.registroInstalacion), name='registroInstalacion'),
     
    
    path('verInstalacion/<id>', views.verInstalacion, name='verInstalacion'),
    path('editaInstalacion/<id>', login_required(views.editaInstalacion), name='editaInstalacion'),
    path('eliminacionInstalacion/<id>', login_required(views.eliminacionInstalacion), name='eliminacionInstalacion'),
   
    path('adminReservas/', views.adminReservas, name='adminReservas'),
    path('registroReservasU/<id>', login_required(views.registroReservasU), name='registroReservasU'), 
    path('eliminacionReserva/<id>', views.eliminacionReserva, name='eliminacionReserva'),


    path('adminHorarios/', login_required(views.adminHorarios), name='adminHorarios'),
    path('registroHorario/', login_required(views.registroHorario), name='registroHorario'), 
    # path('edicionDisiplinas/', views.edicionDisiplinas, name='edicionDisiplinas'),
    # path('editaDisiplina/<id>', views.editaDisiplina, name='editaDisiplina'),
    path('eliminacionHorario/<id>', login_required(views.eliminacionHorario), name='eliminacionHorario'),

    path('pagoonline/<id>', views.pagoonline,name='pagoOnline'),
    path('regpago/', views.regpago,name='regpago'),
    # path('regpago/<data>', views.regpago,name='regpago'),
    # path('regpago/<nombres>,<apellidos>,<ci>,<telefonos>,<correos>,<instalaciones>,<codigos>,<pagos>,<fecha_reservas>,<horarios>', views.regpago,name='regpago'),
    # path('regpago/<nombres>/<apellidos>/<ci>/<telefonos>/<correos>/<instalaciones>/<codigos>/<pagos>/<fecha_reservas>/<horarios>/', views.regpago,name='regpago'),
    #Validaciones 
    re_path(r'^validarFecha/$', views.validarFecha, name='validarFecha'),
    path('reservas_api/', views.reservas_api, name='reservas_api'),

    path('scaner/', views.scaner, name='scaner'),
    path('actualizar_estado/', views.actualizar_estado, name='actualizar_estado'),
    
   ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
