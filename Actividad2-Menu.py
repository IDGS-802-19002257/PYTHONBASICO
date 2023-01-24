import os

class OperarBas:
    # Declaracion de propiedades
    opcion = 0
    num1 = 0
    num2 = 0
    res = 0

    # Declaracion del constructor
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    # Declaracion de metodos de clase
    def suma(self):
        # num1 = 12
        # num2 = 10
        self.res = self.num1 + self.num2
        print('La suma es: {}'.format(self.res))

    def resta(self):
        self.res = self.num1 - self.num2
        print('La resta es: {}'.format(self.res))

    def multi(self):
        self.res = self.num1 * self.num2
        print('La multiplicacion es: {}'.format(self.res))
    
    def divi(self):
        self.res = self.num1 / self.num2
        print('La division es: {}'.format(self.res))

def main():
    os.system('cls')
    opcion = 0
    while opcion != 5:
        print('MENU: \n1.- Suma\n2.- Resta\n3.- Multiplicacion\n4.- Division\n5.- Salir')
        opcion = int(input('Que operacion desea realizar? '))
        if opcion != 5:
            no1 = int(input('Ingrese el primer numero: '))
            no2 = int(input('Ingrese el segundo numero: '))
            obj = OperarBas(no1, no2)

            if opcion == 1:
                obj.suma()
            elif opcion == 2:
                obj.resta()
            elif opcion == 3:
                obj.multi()
            else:
                obj.divi()
        os.system('cls')

if __name__ == '__main__':
    main()