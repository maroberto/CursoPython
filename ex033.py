n1 = int(input('\033[31m Digite um número: '))
n2 = int(input('\033[32m Digite mais um número: '))
n3 = int(input('\033[36m Por favor o último número: '))


maior = n1
menor = n1
# verificando menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('\033[34m O menor número é {} e o maior é {}'.format(menor, maior))


