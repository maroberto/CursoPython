salario = float(input('Qual é o seu salário R$: '))

aumento1 = salario * 0.10
aumento2 = salario * 0.15

if (salario <= 1250.0):
    print('Seu aumento é de R$ \033[32m{:.2f}\033[m e seu salário novo é R$ \033[34m{:.2f} '.format(aumento2, salario+aumento2))
else:
    print('Seu aumento é de R$ \033[31m{:.2f}\033[m e seu salário novo é R$ \033[34m{:.2f} '.format(aumento1, salario+aumento1))
