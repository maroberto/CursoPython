r = 2
lista = []
for i in range(0, 20, 2):
    n1 = i
    lista.append(n1)
if (lista[1] - lista[0]) == r:
    print('O primeiro número da PA é {} e a razão é {}'.format(lista[0], r))
    print('Os 10 primeiros termos são: {}'.format(lista))