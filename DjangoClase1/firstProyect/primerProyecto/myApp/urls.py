from django.contrib import admin
from django.urls import path

#Importar las Views 
from .views import bienvenida, despedida, saludo, saludo_nombre, saludo_con_type, type_name

urlpatterns = [
    path("despedida/",despedida),
    path("",bienvenida),
    path("saludo/",saludo),
    path("saludo/<str:name>",saludo_nombre),
    path("kodemia/<str:name>",saludo_con_type),
    path('kodemia/<str:name>/<str:types>',type_name ),

]
