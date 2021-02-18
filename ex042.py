class Triangulo:
    def __init__(self, reta1, reta2, reta3):
        self.reta1 = reta1
        self.reta2 = reta2
        self.reta3 = reta3

    def Area(self):
        n1 = self.reta1
        n2 = self.reta2
        n3 = self.reta3

        print(10 * '-=-')
        if (n1 + n2 > n3) and (n1 + n3 > n2) and (n3 + n2 > n1):
            print('É um triângulo')
            if (n1 == n2) and (n3 == n1) and (n3 == n2):
                print('Equilátero')
            elif (n1 + n3 > n2):
                print('Isósceles')
            elif (n3 + n2 > n1):
                print('Escaleno')
        else:
            print('Não pode formar triângulo')
        print(10 * '-=-')


tr1 = Triangulo(9, 10, 15)
tr1.Area()
  