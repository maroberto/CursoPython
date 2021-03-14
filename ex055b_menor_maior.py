for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    # verifica o menor e maior(melhor maneira)
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}')
print(f'O menos peso lido fio de {menor}')
