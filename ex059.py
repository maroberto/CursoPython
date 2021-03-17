num1 = float(input('Digite um número: '))
num2 = float(input('Digite mais um número: '))

print(10 * '__')
print('[1]Somar')
print('[2]Multiplicar')
print('[3]Maior')
print('[4]Novos números')
print('[5]Sair do programa')
print(10 * '__')

op = 0
while op != 5:
    op = int(input('Qual é sua opção: '))

    soma = num1 + num2
    mult = num1 * num2
    if op == 4:
        num1 = float(input('Digite um novo número: '))
        num2 = float(input('Digite outro novo número: '))
    if op == 1:
        print(f'A soma dos números é {soma}')
    if op == 2:
        print(f'A produto dos números é {mult}')
    if op == 3:
        maior = num1
        if num2 > maior:
            maior = num2
        print(f'O maior número é {maior}')
print('FIM!')
