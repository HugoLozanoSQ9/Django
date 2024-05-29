from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.




def get_koder(req, idx):
    koders = [
    {"id": 1, "name": "Hugo", "generation": "1G", "bootcamp": "Master Backend con Python"},
    {"id": 2, "name": "Sofía", "generation": "1G", "bootcamp": "Desarrollo Web Full Stack"},
    {"id": 3, "name": "Alejandro", "generation": "2G", "bootcamp": "Desarrollo Frontend con React"},
    {"id": 4, "name": "María", "generation": "1G", "bootcamp": "Desarrollo Mobile con Flutter"},
    {"id": 5, "name": "Diego", "generation": "3G", "bootcamp": "Ciencia de Datos con Python"},
    {"id": 6, "name": "Ana", "generation": "2G", "bootcamp": "Desarrollo Backend con Node.js"},
    {"id": 7, "name": "Javier", "generation": "1G", "bootcamp": "Desarrollo de Videojuegos con Unity"},
    {"id": 8, "name": "Valeria", "generation": "2G", "bootcamp": "Ciberseguridad y Hacking Ético"},
    {"id": 9, "name": "Carlos", "generation": "3G", "bootcamp": "Inteligencia Artificial con TensorFlow"},
    {"id": 10, "name": "Laura", "generation": "1G", "bootcamp": "DevOps y Cloud Computing"},
]
    koder_finded = [ koder for koder in koders if idx == koder['id']]


    return HttpResponse(f"el Id {idx} del koder es: <h1>{koder_finded}</h1>")


def list_koders(req):
    context= {
        "bootcamp":{
            "name":"Python",
            "module":"Django"
        },
        "koders" : [
        {"id": 1, "name": "Hugo", "generation": "1G", "bootcamp": "Master Backend con Python", "is_active":True},
        {"id": 2, "name": "Sofía", "generation": "1G", "bootcamp": "Desarrollo Web Full Stack", "is_active":True},
        {"id": 3, "name": "Alejandro", "generation": "2G", "bootcamp": "Desarrollo Frontend con React", "is_active":True},
        {"id": 4, "name": "María", "generation": "1G", "bootcamp": "Desarrollo Mobile con Flutter", "is_active":False},
        {"id": 5, "name": "Diego", "generation": "3G", "bootcamp": "Ciencia de Datos con Python", "is_active":True},
        {"id": 6, "name": "Ana", "generation": "2G", "bootcamp": "Desarrollo Backend con Node.js", "is_active":True},
        {"id": 7, "name": "Javier", "generation": "1G", "bootcamp": "Desarrollo de Videojuegos con Unity", "is_active":False},
        {"id": 8, "name": "Valeria", "generation": "2G", "bootcamp": "Ciberseguridad y Hacking Ético", "is_active":True},
        {"id": 9, "name": "Carlos", "generation": "3G", "bootcamp": "Inteligencia Artificial con TensorFlow", "is_active":True},
        {"id": 10, "name": "Laura", "generation": "1G", "bootcamp": "DevOps y Cloud Computing", "is_active":False},
        ]
    }

    template = loader.get_template('bootcamp/templates/list_koders.html')


    return HttpResponse(template.render(context,req))
