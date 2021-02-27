print(20 * '__')
numero = int(input('Digite um número: '))
for i in range(1, 31):
    resultado = (numero * i)
    print('{} x {} = {}'.format(numero, i, resultado))
