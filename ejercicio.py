#!/usr/bin/python
#Lucia Villa Martinez

fd=open("/etc/passwd","r")
lineas=fd.readlines()
diccionario = {}

for linea in lineas:
    lista = linea.split(':')
    usuario = lista[0]
    shell = lista[5]
    diccionario[usuario] = shell

try:
    print diccionario["root"]
    print diccionario["imaginario"]

except KeyError:
    print("Lo sentimos, la clave imaginario no existe.")

fd.close()
