from pyspark import SparkContext
import sys
import random

porcentaje = 0.3 #Porcentaje del quijote que queremos coger
archivo_entrada = open('quijote.txt','r')
archivo_salida = open('quijote_s05.txt','w')
for lineas in archivo_entrada:
    dado = random.random()
    if dado <= porcentaje:
        archivo_salida.write(lineas)
archivo_entrada.close()
archivo_salida.close()
