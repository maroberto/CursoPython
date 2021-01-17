from random import randint

numero = randint(1, 100)


if (numero % 2 == 0):
    print('\033[35m O número {} é \033[1;32m PAR!'.format(numero))
else:
    print('\033[35m O número {} é \033[1;34m IMPAR!'.format(numero))






