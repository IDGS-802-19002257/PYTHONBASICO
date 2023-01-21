print('¿Que numero quieres obtener su tabla de multiplicar?')

num = int(input('Escribe un numero: '))

i = 1
for i in range(10):
    print('{} x {} = {}'.format(num, i+1, (num*(i+1))))