class Triangulo:
    def __init__(self,nome, reta1, reta2, reta3):
        self.nome = nome
        self.reta1 = reta1
        self.reta2 = reta2
        self.reta3 = reta3

    def Area(self):
        n1 = self.reta1
        n2 = self.reta2
        n3 = self.reta3

        print(17 * '-=-')
        print('Olá {}'.format(self.nome))

        if (n1 + n2 > n3) and (n1 + n3 > n2) and (n3 + n2 > n1):
            print('É um triângulo')
            if (n1 == n2) and (n3 == n1) and (n3 == n2):
                print('Com todos os lados iguais este é um triângulo Equilátero!')
            elif (n1 == n2) or (n3 == n1) or (n3 == n2):
                print('Com dois lados iguais este é um triângulo isósceles!')
            elif (n1 != n2) and (n3 != n1) and (n3 != n2):
                print('Com todos os lados diferentes este é um triângulo escaleno!')
        else:
            print('Com essas medidas, não se pode formar um triângulo!')
        print(17 * '-=-')


tr1 = Triangulo('Marcos', 11, 11, 175)
tr1.Area()
