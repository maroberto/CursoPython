distancia = int(input('Qual a distância de sua viagem em KM? '))

valor_ate = 0.50
valor_mais = 0.45

if distancia <= 200:
    passagem1 = distancia * valor_ate
    print('O valor de sua passagem é de R$: {:.2F}'.format(passagem1))
else:
    passagem2 = distancia * valor_mais
    print('O valor de sua passagem é de R$: {:.2F}'.format(passagem2))
