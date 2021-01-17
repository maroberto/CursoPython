cidade = str(input('Digite nome da sua cidade: '))
buscar = 'Santo'
nome = cidade.capitalize().split()

if(nome[0] == buscar):
    print('Parabéns o nome de sua cidade começa com Santo!')
else:
    print('O nome da sua cidade começa com {} e não com Santo!'.format(nome[0]))

