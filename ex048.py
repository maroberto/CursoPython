soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i, end=' ')
        cont += 1
        soma += i
print(f'\n\nA soma de todos os {cont} valores solicitados é {soma}!')
