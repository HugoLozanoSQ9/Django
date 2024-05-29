from django.contrib import admin
from django.urls import path

#Importar las Views 
from .views import get_koder,list_koders

urlpatterns = [
    path("koders/<int:idx>",get_koder),
    path('koders/',list_koders)
]