

#El input del algoritmo
""" Tenemos el salario mensual y las horas que trabaja al mes """
salario_mensual=float(input('Ingresa el salario mensual: '))
horario_norma=int(input('ingresa las horas trabajadas en el mes: '))

horario_normal=horario_norma/4
#metodo para resolver el algoritmo
""" En esta funcion defino la tarifa normal y calculo la tarifa que tienes que pagar por las extra horas (Tambien puedes calcular el dinero total si quitamos el 0 que multiplica la tarifa_horario_normal) """
def cal_h_extra(salario_mensual, horario_normal):
    
    tarifa_horario_normal=salario_mensual/horario_normal
    if horario_normal>=36 and horario_normal<=43:
        tarifa_horas_extra=0*(tarifa_horario_normal*35)+(tarifa_horario_normal*(horario_normal-35)*1.25)
    elif horario_normal>=44:
        tarifa_horas_extra=+0*(tarifa_horario_normal*35)+(tarifa_horario_normal*1.25*7)+(tarifa_horario_normal*(horario_normal-43)*1.5)
    else:
        return tarifa_horario_normal==0
    
    return tarifa_horas_extra

#output del algoritmo
""" Aqui te damos el dinero que tienes que pagar por las extra horas """
importe_horas_extra=cal_h_extra(salario_mensual, horario_normal)
print("Este es el dinero que tenemos que pagar al trabajador \npor sus horas extras",importe_horas_extra)