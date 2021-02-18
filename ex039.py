from datetime import date


class Alistamento:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.data_nascimento = ano_nascimento

    def Data(self):
        data_atual = date.today().year
        # data_texto = data_atual.strftime('%d/%m/%y')
        idade = data_atual - self.data_nascimento
        print(20 * '**')
        print('Olá {}'.format(self.nome))
        print('Você nasceu em {}, no ano atual de {}'.format(
            self.data_nascimento, data_atual))
        print('Sua idade é {} anos'.format(idade))

        if idade < 18:
            print(
                'Você tem {} anos e ainda falta {} ano/s para se alistar!'.format(idade, abs(idade - 18)))
        elif idade == 18:
            print('Você tem {} anos  e está na hora de se alistar!'.format(idade))
        else:
            print(
                'Você tem {} anos e passou {} ano/s da hora de se alistar'.format(idade, idade - 18))
        print(20 * '**')


soldado1 = Alistamento(input('Qual é seu nome: '),
                       int(input('Em que ano Você nasceu: ')))
soldado1.Data()
