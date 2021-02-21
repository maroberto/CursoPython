from random import randrange


class Jogo():
    def __init__(self, opcao):
        self.opcao = opcao

    opcao = ('')

    def Computador(self):
        escolha_maquina = randrange(1, 4)
        if (escolha_maquina == 1):
            opcao = ('Pedra')
            print('O computador escolheu {}'.format(opcao))
        elif (escolha_maquina == 2):
            opcao = ('Papel')
            print('O computador escolheu {}'.format(opcao))
        elif (escolha_maquina == 3):
            opcao = ('Tesoura')
            print('O computador escolheu {}'.format(opcao))

        if (escolha_maquina == 1) and (self.opcao == 2):
            print('Papel embrulha predra, você ganhou!')
        elif (escolha_maquina == 2) and (self.opcao == 3):
            print('Tesoura corta papel, você ganhou!')
        elif (escolha_maquina == 3) and (self.opcao == 1):
            print('Pedra quebra tesoura, você ganhou!')
        elif (escolha_maquina == self.opcao):
            print('O jogo empatou!')
        elif (escolha_maquina == 2) and (self.opcao == 1):
            print('Papel embrulha pedra, você perdeu!')
        elif (escolha_maquina == 3) and (self.opcao == 2):
            print('Tesoura corta papel, você perdeu!')
        elif (escolha_maquina == 1) and (self.opcao == 3):
            print('Pedra quebra tesoura, você perdeu!')


print(15 * '-=-')
print('Escolha uma opção\n1) Pedra\n2) Papel\n3) Tesoura')
jogador1 = Jogo(int(input('Pedra, Papel ou Tesoura: ')))
print(15 * '-=-')
jogador1.Computador()
