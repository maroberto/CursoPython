nome = str(input('Digite o seu nome completo: '))

print(nome.upper())
print(nome.lower())

espaco = nome.count(' ')
print('Seu nome tem {} letras'.format(len(nome) - espaco))

pn = nome.split()
print('Seu primeiro nome é {} e tem {} letras!'.format(pn[0], len(pn[0])))


