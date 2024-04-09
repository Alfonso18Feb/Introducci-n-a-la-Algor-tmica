
import os
import time
#el input del algoritmo 
precio=float(input('precio del producto sin impuestos:'))
print('IVA es un porcentage')
IVA=float(input('El IVA del producto:'))
# el metodo para resolver el algoritmo
def impuesto(precio, IVA):
    return(precio+((IVA/100)*precio))#sumamos la IVA
# El output del algoritmo
print('precio del producto con TII:',impuesto(precio,IVA))
time.sleep(12)
os.system('cls')
print('2.calcula el importe de los intereses generados por un capital invertido a un interés dado\n durante un tiempo dado, expresado en meses.')
print(" ")
#input de la segunda parte del algoritmo
cap_inv=float(input("El capital invertido es: "))
interes_m=float(input("El porcentage del interes mensual es: "))
Nºmeses=int(input("Numero de meses que esta el dinero en el banco es: "))

#El metodo utilizado para resolver el algoritmo
def Ingen(cap_inv,interes_m,Nºmeses):
    return(cap_inv*(interes_m/100)*Nºmeses)#formula para ingreso generado
#El resultado o output de nuestro algoritmo
print('el importe generado es: ',Ingen(cap_inv,interes_m,Nºmeses))