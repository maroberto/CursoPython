primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

c = 0
fatorial = primeiro
print(primeiro, end='! ')
while c != 9:
    fatorial = fatorial + razao
    c += 1
    print(f'{fatorial}', end=' → ')
print('ACABOU')
