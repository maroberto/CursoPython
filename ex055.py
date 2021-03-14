pesos = []
for i in range(0, 5):
    peso = float(input(f'Peso da {i} pessoa: '))
    pesos.append(peso)
print(20 * ('__'))

n1 = pesos[0]
n2 = pesos[1]
n3 = pesos[2]
n4 = pesos[3]
n5 = pesos[4]

maior = n1
menor = n1
# verificando menor
if n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    menor = n2
if n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
    menor = n3
if n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
    menor = n4
if n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
    menor = n5
# verificando maior
if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    maior = n2
if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    maior = n3
if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    maior = n4
if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    maior = n5
print(f'O maior peso lido foi {maior}kg')
print(f'O menor peso lido foi {menor}kg')
