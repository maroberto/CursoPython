from datetime import date

data_atual = date.today().year # verifica o ano atual
print(data_atual)
maior = 0
menor = 0
for i in range(1, 7):
    ano_nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    if data_atual - ano_nascimento < 21:
        menor += 1
    else:
        maior += 1
print(f'Temos {menor} pessoas menores de idade\ne {maior} pessoas maiores de idade: ')
 