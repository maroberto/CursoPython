n = int(input('Digite um número para ver sua tabuada: '))


print('____________')
i = 1
while (i <= 11):
    print('{} X {:2} = {}'.format(n, i, (n * i)))
    i = i + 1
    if(i == 11):
        break
print('____________')
