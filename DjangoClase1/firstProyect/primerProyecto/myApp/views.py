from django.shortcuts import render
from django.template import loader

# importar HTTPResponse
from django.http import HttpResponse

# Create your views here.

# Las vistas son declaradas como funciones
# El cliente --> Pide --> Request
# Servidor --> Response --> Response


def bienvenida(request):
    # responder
    return HttpResponse("Bienvenido")


def despedida(req):
    return HttpResponse("Adios")


def saludo(req):
    return HttpResponse("Saludando a los Koders")


def saludo_nombre1(req, name):
    return HttpResponse(f"Saludando a: {name}")


def saludo_con_type(req, name):
    name = name.lower()
    if name == "mentor":
        return HttpResponse(f"Hola {name} aquí están tus clases")
    elif name == "koder":
        return HttpResponse(f"Hola {name} welcome to kodemia")
    else:
        return HttpResponse(f"You are not welcome here {name} go away!!")


#Antes de modificar los contextos
# Forma de renderizar templates
#def saludo_nombre(req, name):
#   context = {"name": name}  # Va a servir para pasarle info al template
#    template = loader.get_template(
#        "base.html"
#    )  # Solo se pone el base.html por que ya tenemos conigurados los templates en settings.py
#    return HttpResponse(template.render(context, req))
    
def saludo_nombre(req, name):
    context = {"name": name} # Va a servir para pasarle info al template
    template = loader.get_template(
            "templates/base.html"
    )  # Solo se pone el base.html por que ya tenemos conigurados los templates en settings.py
    return HttpResponse(template.render(context, req))


def type_name(req, name, types):
    context = {"name": name, 
               "apellido":"Lozano jeje",
               "type": types}
    template = template = loader.get_template("base.html")
    return HttpResponse(template.render(context, req))
