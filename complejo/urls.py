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
from reservas.views import LoginFormView,LogoutView
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    path('', LoginFormView.as_view(),name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),

    path('instalaciones/', views.instalaciones, name='instalaciones'),
    path('detalleInstalacion/<id>', views.detalleInstalacion, name='detalleInstalacion'),
    path('registroReservasU/<id>', views.registroReservasU, name='registroReservasU'),

    path('adminDisiplinas/', views.adminDisiplinas, name='adminDisiplinas'),
    path('registroDisiplina/', views.registroDisiplina, name='registroDisiplina'), 
    path('edicionDisiplinas/', views.edicionDisiplinas, name='edicionDisiplinas'),
    path('editaDisiplina/<id>', views.editaDisiplina, name='editaDisiplina'),
    path('eliminacionDisiplina/<id>', views.eliminacionDisiplina, name='eliminacionDisiplina'),
     

    path('adminInstalaciones/', views.adminInstalaciones, name='adminInstalaciones'),
    path('registroInstalacion/', views.registroInstalacion, name='registroInstalacion'), 
    
    path('verInstalacion/<id>', views.verInstalacion, name='verInstalacion'),
    path('editaInstalacion/<id>', views.editaInstalacion, name='editaInstalacion'),
    path('eliminacionInstalacion/<id>', views.eliminacionInstalacion, name='eliminacionInstalacion'),
   
    path('adminReservas/', views.adminReservas, name='adminReservas'),
    path('registroReservas/<id>', views.registroReservas, name='registroReservas'), 


    path('adminHorarios/', views.adminHorarios, name='adminHorarios'),
    path('registroHorario/', views.registroHorario, name='registroHorario'), 
    # path('edicionDisiplinas/', views.edicionDisiplinas, name='edicionDisiplinas'),
    # path('editaDisiplina/<id>', views.editaDisiplina, name='editaDisiplina'),
    # path('eliminacionDisiplina/<id>', views.eliminacionDisiplina, name='eliminacionDisiplina'),

    #path('pagoonline/<id>', views.pagoonline,name='pagoOnline'),
    # path('regpago/<data>', views.regpago,name='regpago'),
    # path('regpago/<nombres>,<apellidos>,<ci>,<telefonos>,<correos>,<instalaciones>,<codigos>,<pagos>,<fecha_reservas>,<horarios>', views.regpago,name='regpago'),
    # path('regpago/<nombres>/<apellidos>/<ci>/<telefonos>/<correos>/<instalaciones>/<codigos>/<pagos>/<fecha_reservas>/<horarios>/', views.regpago,name='regpago'),
    #Validaciones 
    re_path(r'^validarFecha/$', views.validarFecha, name='validarFecha'),
    path('reservas_api/', views.reservas_api, name='reservas_api'),
    
   ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
