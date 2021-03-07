frase = str(input('Digite uma frase: '))
print(' Você digitou: {}'.format(frase))

if frase.count(' '):
    frase = frase.replace(' ', '')
    string = frase[::-1] # inverte a string
    print('A frase que você digitou invertida fica: {}'.format(string))
    if frase == string:
        print('É um palíndromo')

# anotaram a data da maratona
# apos a sopa
# a torre da derrota
# o bolo ama o bolo
# 