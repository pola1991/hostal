from django.urls import path
from .views import *


urlpatterns = [
    path('',home, name='home'),
    path('login/', login, name='login'),
    path('loginEmpresa/', loginEmpresa, name='loginEmpresa'),
    path('registroCliente/', registroCliente, name='registroCliente'),
    #path('registroEmpresa/', registroEmpresa, name='registroEmpresa'),
    path('perfilCliente/', perfilCliente, name='perfilCliente'),
    path('addProveedor/', addProveedor, name='addProveedor'),
    path('readProveedor/', readProveedor, name='readProveedor'),
    
]