from datetime import date

data_atual = date.today().year
print(data_atual)
maior = 0
menor = 0
for i in range(1, 7):
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    if data_atual - ano_nascimento < 21:
        menor += 1
    else:
        maior += 1
print(f'Menor idade: {menor} / Maior idade: {maior}')
