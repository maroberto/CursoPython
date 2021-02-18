class Alunos:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def Media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        print(30 * '__')
        print('Olá {}!'.format(self.nome))
        if (media < 5.0):
            print(
                'Sua média é {:.1f} infelismente você foi reprovado!'.format(media))
        elif (media < 7.0):
            print(
                'Sua média é {:.1f} você está de recuperacão!'.format(media))
        else:
            print(
                'Sua média é {:.1f} parabéns você está aprovado!'.format(media))
        print(30 * '__')

'''
aluno1 = Alunos(input('Digite seu nome: '),  float(input('Digite a primeira nota: ')), float(input(
    'Digite e segunda nota: ')), float(input('Digite a terceira nota: ')))
aluno1.Media()


aluno2 = Alunos(input('Digite seu nome: '),  float(input('Digite a primeira nota: ')), float(input(
    'Digite e segunda nota: ')), float(input('Digite a terceira nota: ')))
aluno2.Media()
'''
