numero = int(input('Digite um número: '))
d = numero * 2
t = numero * 3
r = numero ** (1 / 2)

print('O dobro de {} vale {}. '.format(numero, d))
print('O triplo de {} vale {}. '.format(numero, t))
print('A raiz quadrada de {} é igual a  {:.2f}. '.format(numero, r))
print('A raiz quadrada de {} é igual a  {:.2f}. '.format(numero, pow(numero, (1 / 2))))

# (numero, pow (numero, (1/2)) também calcula a raiz quadrada
