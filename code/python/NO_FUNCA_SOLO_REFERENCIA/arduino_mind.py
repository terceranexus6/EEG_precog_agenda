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
salir = False
arduino = serial.Serial(device, 9600)

#crear un archivo para el log
file = open("testfile_lectura.txt","w")


while salir == False:

	valor = arduino.readline()
	#muestra por pantalla
	print ("Writing on file...")
	print (valor)
	#meter en log el contenido
	file.write("Value:")
	file.write(valor)

	#definimos contraseña
	str1 = randrange(21863)
	if valor > 40 and valor < 50:
		contra = 'qoiwubhftayoooui'
	else:
		contra = 'osidapojanasakhv'
	con = con +1

	if con == 30:
		salir = True


#cerramos el log
file.close()

nombre = "clave"+".txt"

create_f="touch "+nombre
command = "sudo gpg --yes --batch --cipher-algo AES256 --passphrase=["+contra+"] -c "+nombre
command2 = "rm -rf "+nombre

print ("la contraseña seria: ")
print (contra)

print("el comando seria: ")
print (command)

#create the file
#subprocess.call(create_f, shell=True)

#encrypt with passphrase
subprocess.call(command, shell=True)

#delete the message
#subprocess.call(command2, shell=True)
