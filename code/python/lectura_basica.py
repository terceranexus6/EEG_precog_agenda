#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import numpy as np
import time
import random
import serial
import sys
from random import randrange
import subprocess

#conectarse al arduino en el puerto que corresponda
device='/dev/ttyACM0'
print "Trying to connect"
arduino = serial.Serial(device, 9600,timeout=2)

#valor = arduino.readline()
#print (valor)

#topes
#topeA = 10
topeB = 30
topeC = 50
topeD = 100
#topeE = 80


tarea1 = "Escribir nota de la compra"
tarea2 = "Mandar mensaje a Fulanito"
tarea3 = "Contestar correo del profesor"
tarea4 = "Hacer la práctica"
tarea5 = "Trabajar"

# listas para la agenda, 5 actividades
agenda = [tarea1,tarea2,tarea3,tarea4,tarea5]
#print (agenda[0])
dificultad = [1,2,3,4,5]

#con = 0

print "Asegúrate de tener el casco bien colocado. "
recordatorio=raw_input("Introduce cada cuanto quieres el recordatorio (en segundos): ")
recordatorio=int(recordatorio)

'''
while (con < 5):
	agenda[con]=raw_input('Introduce la tarea: ')
	difi=raw_input('Introduce la dificultad de la tarea (de 0 a 5):')
	dificultad[con]=int(difi)

	con = con + 1

con = 0
while (con < 5):
    print agenda[con]
    print dificultad[con]
    con = con + 1
'''





#crear un archivo para el log
file = open("testfile_lectura.txt","w")


while(True):

    valor = arduino.readline()
    file.write(valor)

    #probando
    print(valor)
    time.sleep(1)

    if (int(valor) < topeB):
        print "Tu concentracion es actualmente baja."
        print "Actividad recomendada..."
        print agenda[0]
        utarea = agenda[0]

    elif (int(valor) > topeB and int(valor) < topeC):
        print "Tu concentracion es actualmente media."
        print "Actividad recomendada..."
        print agenda[1]
        utarea = agenda[1]

    else:
        print "Tu concentracion es actualmente alta."
        print "Actividad recomendada..."
        print agenda[2]
        utarea = agenda[2]

    time.sleep(recordatorio)

    '''
    respuesta = int(raw_input("¿Has acabado? 0/1: "))

    while(respuesta == 0 or respuesta == 0):
        time.sleep(recordatorio)
        respuesta = int(raw_input("¿Has acabado? 0/1: "))
    '''
