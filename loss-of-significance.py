# -*- coding: utf-8 -*-
"""
Created on Sun Aug 04 20:24:05 2019

@author: Felipe Lorca

CALCULO DE VOLUMENES DE SITEMA SOLAR

"""
import numpy as np
from matplotlib import pyplot as plt

def Volumen(r):
    v=(4.0/3.0)*np.pi*(r**3.0)
    return v

def radio(v):
    r=(3.0*v/(4.0*np.pi))**(1.0/3.0)
    return r
# Radios medio de planetas en Km
radios = {"Mercurio":2439.7,"Venus":6051.8,"Tierra":6371.0,"Marte":3389.5,"Jupiter":69911.0,"Saturno":58232.0,"Urano":25362.0,"Neptuno":24622.0}

#listas con volumenes
keys = []
float16 = [] #lista float16
float32 = [] #lista float32
float64 = [] #lista float64
error16 = []
error32 = []
error64 = []
res16 = []
res32 = []
res64 = []
for key in (radios): #Tomamos una rango de 5 numeros de variacion
    keys.append(key)
    float16.append(np.float16(Volumen(radios[key])))
    float32.append(np.float32(Volumen(radios[key])))
    float64.append(np.float64(Volumen(radios[key])))

for i in range(len(float16)):
    res16.append(radio(float16[i]))
    res32.append(radio(float32[i]))
    res64.append(radio(float64[i]))
    error16.append(abs(radio(float16[i])-radios[keys[i]])/radios[keys[i]])
    error32.append(abs(radio(float32[i])-radios[keys[i]])/radios[keys[i]])
    error64.append(abs(radio(float64[i])-radios[keys[i]])/radios[keys[i]])

#output
print "Usando float16\n"
for i in range(len(keys)):
    print keys[i],"valor real =",radios[keys[i]],"valor calculado =",res16[i],"(error =",str(error16[i])+" )"

print "\nUsando float32\n"
for i in range(len(keys)):
    print keys[i],"valor real =",radios[keys[i]],"valor calculado =",res32[i],"(error =",str(error32[i])+" )"

print "\nUsando float64\n"
for i in range(len(keys)):
    print keys[i],"valor real =",radios[keys[i]],"valor calculado =",res64[i],"(error =",str(error64[i])+" )"

a=[]
for i in keys:
    a.append(radios[i])
    
#Plot 

#plt.plot(a,error16, 'r')
#plt.plot(a,error32, 'b')
#plt.plot(a,error64, 'g')
#plt.axis([ min(a) , max(a) , min(error64) , max(error32) ] )
#plt.xlabel('Radio real en Km')    
#plt.ylabel('Error relativo')
#plt.legend(["error float16","error float32","error float64"])
#plt.title("Perdida de significancia") 
#plt.show()

