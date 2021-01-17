from random import randint
from time import sleep

numero = randint(1, 5)
print('-=-' * 10)
palpite = int(input('Digite um número de 0 a 5: '))

print('PROCESSANDO...')
sleep(3)
if palpite == numero:
    print('Parabéns você acertou!')
else:
    print('Infelizmente você errou!')
