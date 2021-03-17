num = int(input('Digite um número: '))
contador = num
while contador != 0:
    fatorial = num * (contador - 1) 
    resultado = fatorial * contador - 1
    # contador = contador - 1
    # resultado = num * contador
    # resultado2 = resultado * (contador - 1)
    # print(contador,num, resultado, resultado2)
    print(fatorial, resultado)