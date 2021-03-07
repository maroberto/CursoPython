class Soma():
    def __init__(self, numeros):
        self.numeros = numeros

    def Calculo(self):
        s = 0
        for i in range(0, 6):
            self.numeros
            if (self.numeros % 2) == 0:
                s += self.numeros
                print('Resultado é {}'.format(s))
            else:
                print('Número impar não somado!')


primeiro = Soma(int(input('Digite um numero: ')))
primeiro.Calculo()
