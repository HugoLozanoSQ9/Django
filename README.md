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

