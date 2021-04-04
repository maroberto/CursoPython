primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))


c = 0
fatorial = primeiro
print(primeiro, end='! ')
ver_mais = 9
while ver_mais != 0:
    fatorial = fatorial + razao
    c += 1
    print(f'{fatorial}', end=' → ')
    if c == ver_mais:
        mais = int(
            input('Quer ver mais quantos termor digite [0] P/ encerrar  '))
        if mais != 0:
            ver_mais = (ver_mais + mais)
        else:
            ver_mais = mais
print('ACABOU!')
