n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))


if n1 > n2:
    print('O primeiro número \033[35m{}\033[m é maior que o segundo \033[35m{}\033[m!'.format(n1, n2))
elif n2 > n1:
    print('O segundo número \033[35m{}\033[m é maior que primeiro \033[35m{}\033[m!'.format(n2,n1))
else:
    print('Os dois números são iguais \033[36m1°\033[m {} \033[36m2°\033[m {}'.format(n1, n2))
