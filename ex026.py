frase = str(input('Digite uma frase: '))

primeira = frase.upper().count('A')
print('Sua Frase tem {} letras "A"'.format(primeira))

print('A letra "A" aparece a primeira vez na posição {}'.format(frase.upper().find('A')))

print('A letra "A" aparece pela última vez na posição {}'.format(frase.upper().rfind('A')))




