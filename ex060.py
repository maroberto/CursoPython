# from math import factorial


# num = int(input('Digite um número: '))
# print(factorial(num))

n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}!', end=' = ')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f'{f}')
