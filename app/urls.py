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
    path('eliminarProveedor/<int:id>/',eliminarProveedor,name='eliminarProveedor'),
    path('hab',hab,name='hab'),
    path('formu_create',formu_create,name='formu_create'),
    path('formu_update/<int:id>', formu_update, name='formu_update'),
    path('formu_delete/<int:id>/', formu_delete, name='formu_delete'),
    path('huespedes',huespedes,name='huespedes'),
    path('formu_createh',formu_createh,name='formu_createh'),
    path('formu_updateh/<int:id>', formu_updateh, name='formu_updateh'),
    path('formu_deleteh/<int:id>/', formu_deleteh, name='formu_deleteh'),
    
]
