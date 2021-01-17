print('\033[31m-=-'*20)
print('\033[34mAnalisador de triangulos')
print('\033[31m-=-\033[m'*20)

n1 = float(input('Digite o comprimento da reta 1: '))
n2 = float(input('Digite o comprimento da reta 2: '))
n3 = float(input('Digite o comprimento da reta 3: '))

if (n1 + n2 > n3) and (n1 + n3 > n2) and (n3 + n2 > n1):
    print('\033[34mPode formar um triangulo')
else:
    print('\033[31mNão pode formar um triangulo')
