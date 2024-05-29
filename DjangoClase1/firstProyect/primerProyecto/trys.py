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

idx = 5

for koder in koders:
    if idx == koder['id']:
        print(koder)
