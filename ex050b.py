s = 0
cont = 0
for i in range(1, 7):
    numeros = int(input('Digite o {} valor: '.format(i)))
    if (numeros % 2) == 0:
        s += numeros
        cont += 1
print(8 * '--=--')
print(f'Você digitou {cont} números pares a a soma é {s}!')
