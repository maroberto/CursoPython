# retira espacos e transforma em maiuscula
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
print(f'O inverso de {frase} é {frase[::-1]}')# inverte a string

if frase == frase[::-1]:
    print('Temos um palíndromo')

inverso = ''
for letra in range(len(frase) -1, -1, -1):
    inverso += frase[letra]
if inverso == frase:
    print('Temos um Palíndromo')
else:
    print('Não é um Palíndromo') 

# anotaram a data da maratona
# apos a sopa
# a torre da derrota
# o lobo ama o bolo
