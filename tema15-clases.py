import os

class OperarBas:
    # Declaracion de propiedades
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

def main():
    os.system('cls')
    obj = OperarBas(3,4)
    obj.suma()

if __name__ == '__main__':
    main()


# class OperarBas:
#     # Declaracion de propiedades
#     num1 = 0
#     num2 = 0
#     res = 0

#     # Declaracion del constructor
#     def __init__(self):
#         pass

#     # Declaracion de metodos de clase
#     def suma(self):
#         num1 = 12
#         num2 = 10
#         res = num1 + num2
#         print('La suma es: {}'.format(res))

# def main():
#     obj = OperarBas()
#     obj.suma()

# if __name__ == '__main__':
#     main()