contagem = 0
for i in range(1, 500, 2):
    de = 3
    multiplo = (de * i)
    natural = (multiplo / de)
    numero = (i % 3) == 0
    contagem = contagem + 1
    # print(numero, i, contagem)
    print('{}   > {} X {} = {} / {} = {}'.format(contagem, de, i, multiplo, int(natural), de))
