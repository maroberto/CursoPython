from random import randint


numero = randint(0, 10)
print('--' * 15)
contador = 0
palpite = 11
while palpite != numero:
    contador += 1
    palpite = int(input('O número que você pesou foi: '))
print('--' * 15)
print(f'Você acertou na {contador}ª tentativa')
