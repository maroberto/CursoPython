import math

co = int(input('Digite o comprimento do cateto oposto: '))
ca = int(input('Digite o comprimento do cateto adjacente: '))

b = math.pow(co, 2)
c = math.pow(ca, 2)
a = (b + c)

print('O comprimento sa hipotenusa é {:.2f}'.format(math.sqrt(a)))
