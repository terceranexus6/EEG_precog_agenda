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
arduino = serial.Serial(device, 9600,timeout=2)

valor = arduino.readline()
#print (valor)

while(True):

    print(valor)
    time.sleep(1)
