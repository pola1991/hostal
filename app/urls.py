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
    path('addComedores/', addComedores, name='addComedores'),
    path('readComedor/', readComedor, name='readComedor'),
    path('eliminarComedor/<id>/', eliminarComedor, name='eliminarComedor'),
    path('eliminarProveedor/<id>/',eliminarProveedor,name='eliminarProveedor'),
    path('hab',hab,name='hab'),
    path('formu_create',formu_create,name='formu_create'),
    path('formu_update/<int:id>', formu_update, name='formu_update'),
    path('formu_delete/<int:id>/', formu_delete, name='formu_delete'),
    
]
