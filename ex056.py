soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher_20 = 0


for p in range(1, 5):
    print(f'_____ {p}ª Pessoa _____')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: ')) 
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    # verifica o mais velho e mais novo
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1


media_idade = soma_idade / 4
print('A média da idade do grupo é de {:.2f} anos'.format(media_idade))
print('O Homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_mulher_20))