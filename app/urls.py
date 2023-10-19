from django.urls import path
from .views import *


urlpatterns = [
    path('',home, name='home'),
    path('login/', login, name='login'),
    path('registroCliente/', registroCliente, name='registroCliente'),
    path('registroEmpleado/', registroEmpleado, name='registroEmpleado'),
    path('perfilCliente/', perfilCliente, name='perfilCliente'),
    path('addProveedor/', addProveedor, name='addProveedor'),
    path('readProveedor/', readProveedor, name='readProveedor'),
    
]