import math
import os
import time
print("1. Escribir un algoritmo que calcula la media aritmética de tres números dados")
print('\t')
""" Aqui se pone el input del algoritmo. Se pone los tres números dados. """

x=float(input('nota de alumno1 :'))
y=float(input('nota de alumno2 :'))
z=float(input('nota de alumno3 :'))
""" La funcion es las instruciones que sigue el programa """
def media(x,y,z):
    return((x+y+z)/3)
os.system ("cls")
time.sleep(0.2)

""" la salido o output del algoritmo """
print("media aritmetica nota de alumnos:",media(x,y,z))
time.sleep(5)
os.system ("cls")

print('2.Una media ponderada cuando se dan los números y los coeficientes de\n ponderación.')
print('\t')
print('separalos con " " espacio')
#el input del algoritmo
numero=(input('escribe los numeros de las notas:')).split()
print("Escribe las notas y el ponderado en el mismo orden")
ponderado=(input('escribe los ponderados de las notas:')).split()
'''comprobamos que es una lista de enteros y float '''
numero = list(map(int, numero))
ponderado = list(map(float, ponderado))

#el metodo del algoritmo 
def mediaponderada(numero ,ponderado):
    numpondera=list(map(lambda x, y: x * y, numero, ponderado))
    #juntamos ambas listas y multiplicamos numero[n]*ponderado[n]
    return(sum(numpondera)/sum(ponderado)) #formula de media ponderada
#output del algoritmo
print('la media ponderada es:',mediaponderada(numero ,ponderado))