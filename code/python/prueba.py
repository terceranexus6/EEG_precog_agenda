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
device='/dev/ttyACM1'
print "Trying to connect"
con = 0
salir = 0
arduino = serial.Serial(device, 9600)

# listas para la agenda, 5 actividades
agenda = ['a','b','c','d','e']
print (agenda[0])
dificultad = [0,0,0,0,0]

con = 0

recordatorio=raw_input("Introduce cada cuanto quieres el recordatorio (en segundos): ")
recordatorio=int(recordatorio)

while (con < 5):
	agenda[con]=raw_input('Introduce la tarea: ')
	difi=raw_input('Introduce la dificultad de la tarea (de 0 a 5):')
	dificultad[con]=int(difi)

	con = con + 1

#crear un archivo para el log
file = open("testfile_lectura.txt","w")

#crear topes de concentracion

#topeA = 10
topeB = 30
topeC = 50
#topeD = 70
#topeE = 80

#ultima tarea
utarea = 0


while (salir < 4):

	valor = arduino.readline()
	#muestra por pantalla
	print ("Writing on file...")
	print (valor)
	#meter en log el contenido
	file.write("Value:")
	file.write(valor)


#	if (valor < topeB):
#		for x in dificultad:
#			if (dificultad[x] < 2):
#				print agenda[x]
#				print "Tu concentracion es actualmente baja."
#				utarea = x
#	elif (valor > topeB and valor < topeC):
#		for x in dificultad:
#			if (dificultad[x] >= 2 and dificultad[x] <= 3):
#				print agenda[x]
#				print "Tu concentracion es actualmente media."
#				utarea = x
#	else:
#		for x in dificultad:
#			if (dificultad[x] >= 4):
#				print agenda[x]
#				print "Tu concentracion es actualmente alta."
#				utarea = x



	time.sleep(recordatorio)

	salir = salir + 1
	print("iteracion...")
	print salir


#cerramos el log
file.close()
