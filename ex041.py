from datetime import date


class Atleta:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def Categoria(self):
        data_atual = date.today().year
        idade = data_atual - self.data_nascimento

        print(20 * '--')
        print('Olá {} '.format(self.nome))
        if (idade <= 9):
            print('Você tem {} e é da categoria mirim!'.format(idade))
        elif (idade <= 14):
            print('Você tem {} e é da categoria infantil!'.format(idade))
        elif (idade <= 19):
            print('Você tem {} e é da categoria junior!'.format(idade))
        elif (idade <= 20):
            print('Você tem {} e é da categoria sênior!'.format(idade))
        else:
            print('Você tem {} e é da categoria master!'.format(idade))
        print(20 * '--')


atleta1 = Atleta('Fernando', 2012)
atleta1.Categoria()

atleta2 = Atleta('Carlos', 2008)
atleta2.Categoria()

atleta3 = Atleta('Juvenal', 2004)
atleta3.Categoria()

atleta4 = Atleta('Frederico', 2001)
atleta4.Categoria()

atleta5 = Atleta('Rodolfo', 2000)
atleta5.Categoria()
