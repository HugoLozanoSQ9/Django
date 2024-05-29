# ¿Por qué Django?

Desing philosophies
-Debilmente acoplado 
-Menos códgo
-Don´t repeat yourself
-Quick development
-Explicit is better than implicit


## arquitectura MVC
modelo vista y controlador 

usuario -><- server -> <- Controlador -> vista -> modelo -->Db
                                      -> modelo --Db

## Arquitectura MVT

Modelo vista Template 
Esta vista es ocupada por Django
user --> Django Framwkork --><-- Url --><-- |View --><-- Model  | --> data
                                            |View--><-- Template| --> data
## RECORDANDO PYTHON

__init__ emn una clase es el constructor
en cambio el __init__ dentro de una carpeta significa que esa carpeta es un paquete de python

# Comenzar a usar el virtual env

virtualenv venv

# Activar venv

source venv/bin/activate

# crear nuevo proyecto 
django-admin startproject [Nombre del proyecto]

# Una vez creado se debe migrar todo
python3 manage.py migrate

# Crear super usuario para el server localhost/admin
python3 manage.py createsuperuser

username: admin
emailAdd:hugolkii@gmail.com
password: 1234567890

# Crear una app
python manage.py startapp myApp

# Hay 2 tipos de renderización

Client rendering

SSR (server site rendering) (Django se tiene que hacer por parte del SSR)

Se pueden implementar sistemas separados (tener frontend en una parte y el backend en otra parte)

## Cliente rendering 

Cuando se reciben datos por decir de una API y lo pinta con HTML CSS y JS de manera dinámica

## SSR

Todos los datos ya se encuentran dentro de la aplicación ya no se reciben datos de otra parte

## Pasos para crear views 
ingresamos las views de mi app --> generamos la función de la view --> vamos a urls --> la importamos  --> y la agregamos en urlpatterns 

def saludo(req):
    return HttpResponse('Saludando a los Koders')

path("saludo/",saludo)

# URL's dinámicas
Al crear la función se agrega como argumento el parámetro de la URL que vamos a hacer dinámica

def saludo_nombre(req,name):
    return HttpResponse(f"Saludando a {name}")

Al momento de definir la url debemos agregarle el <str:algo> por ejemplo:

### Es importante recordar que debemos nombrar la variable exactamente igual a el argumento de la función 
path("saludo/<str:name>",saludo)

# URL's en my app

Debemos modular las url's por app entonces se hará por app esto en cada app creando 
urls.py
en este archivo dentro de la app se deben pegar las vistas hechas anteriormente y borrarlas desde la carpeta principal 

#### Inluir las URL's externas 
Dentro de mi proyecto principal tenemos que importar includes (seguido del path) y proceder con la siguiente linea de códugo
En donde si el primer argumento lo dejo como una cadena vacía entonces continuará como estaba nativamente, en cambio si yo pongo algo diferente como 
"algo/" las rutas se van a anidar a ese algo quedando: algo/saludar
path("",include("myApp.urls")),
path("saludos/",include("myApp.urls"))


## Configurando nuestros templates
Fuimos a la carpeta principal, ingresamos a settings.py --> ubicamos la variable TEMPLATES y en la propiedad DIRS: se hizo esto 
[os.path.join(BASE_DIR,"myApp","templates")]
BASE_DIR es el directorio por default, pero si queremos que tengamos ciertos templates por app entonces debemos hacer un join 
(el join nos separa con / todo lo que esté anidado con "," comas)
para esto dentro de myApp se creó un directorio de templates


# Renderizar HTML
primero definimos nuestras vistas

#Forma de renderizar templates
def saludo_nombre(req,name):
    context = {"name":name} #Va a servir para pasarle info al template
    template = loader.get_template("base.html") #Solo se pone el base.html por que ya tenemos conigurados los templates en settings.py
    return HttpResponse(template.render(context,req))

Dentro de context se encuentra toda la información que vamos a llenar dentro de mi HTML
En template se ubica la ruta de los templates y se asigna el nombre correspondiente del template

Ya solo se renderiza en la respuesta HTML

# DTL - TAGS
Django template Lenguage
{%tag%} {%endtag%}

para mejor entendimiento ir a bootcamp --> templates --> list_koders.html