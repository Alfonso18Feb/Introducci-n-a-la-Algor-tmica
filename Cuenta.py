import os
#input de todos los datos para que funcione el algoritmo
saldo=input('El saldo en tu cuenta bancaria: ')
id_banco=input('EL numero de identidad bancario: ')
retira=input('lo que quieres retirar de tu cuenta bancaria es: ')
#metodo esta dentro de la clase
class cuenta():
    def __init__(self,saldo,id_banco,retira):
        self.saldo=saldo
        self.id_banco=id_banco
        self.retira=retira
    def get_id_banco(self):
        if isinstance(self.id_banco,str):
            return self.id_banco
        else:
            TypeError('tipo string')
    def get_saldo(self):
        if isinstance(self.saldo,float):
            return self.saldo
        else:
            TypeError('tipo float')
    def get_retira(self):
        if isinstance(self.retira,float):
            return self.retira
        else:
            TypeError('Tiene que ser un float')
    def set_saldo(self,saldo):
        self.saldo=saldo
    def retir(saldo,retira):
        if saldo>retira:
            return(saldo-retira)   
        else:
                ValueError('saldo tiene que ser positivo para retirar de la cuenta')
    def __str__(self):
        return 'El id de tu cuenta bancaria es:'+str(self.id_banco)+'\n TU saldo es de:'+str(self.saldo)+'\n has retirarado:'+str(self.retira)
#El output deuelve el __str__ de la clase
c=cuenta(saldo,id_banco,retira)
os.system("cls")
print(c)


