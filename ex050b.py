s = 0
for i in range(0, 6):
    numeros = int(input('Digite um Número: '))
    if (numeros % 2) == 0:
        s += numeros
        print('Resultado é {}'.format(s))
    else:
        print('Número impar não somado!')
