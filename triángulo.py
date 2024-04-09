import time
import os
""" 
1. Escribir un algoritmo que calcula el área de un triángulo del que se da la medida de un lado y la de la altura relativa a este lado. """
#el input del algoritmo de area del triangulo

altura=float(input('altura del triangulo es: '))
lado=float(input('medida de un lado es: '))
#el metodo para resolver dicho algoritmo
def areaTria(altura,lado):
    return((altura*lado)/2)
#output de algoritmo
print('area del triangulo de lado {} y altura {} es de:'.format(lado,altura),areaTria(altura,lado))
time.sleep(13)
os.system("cls")
#respuesta para el segundo apartado del ejercicio
print("perguntas frecuentes")
print('')
print('2. ¿Se puede utilizar este algoritmo para un triángulo rectángulo\n si se dan las medidas de sus dos lados perpendiculares?')
print('')
print("SI")