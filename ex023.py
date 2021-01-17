numero = int(input('Digite um número inteiro, ex. 0 a 9999: '))

if(numero <= 9):
    print('unidade: {}'.format(numero))
elif(numero <= 99):
    print('dezena: {}'.format(numero))
elif(numero <= 999):
    print('centena: {}'.format(numero))
else:
    print('milhar: {}'.format(numero))






