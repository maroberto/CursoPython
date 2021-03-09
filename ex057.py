n1 = 102
n2 = 150
n3 = 55
n4 = 78
n5 = 90

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
print(maior, menor)
