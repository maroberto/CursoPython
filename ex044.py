class Vendas():
    def __init__(self, produto, valor, forma_pagamento):
        self.produto = produto
        self.valor = valor
        self.forma_pagamento = forma_pagamento

    def Pagamanto(self):
        print(37 * '-=-')
        if self.forma_pagamento == 1:
            desconto = self.valor - (self.valor * 0.10)
            print('Olá você comprou um/a {}, com pagamento em dinheiro seu desconto é de 10%. O Valor a Pagar é: R$ {:.2f}'.format(self.produto, desconto))
        elif self.forma_pagamento == 2:
            desconto = self.valor - (self.valor * 0.05)
            print('Olá você comprou um/a {}, com pagamento avista no cartão seu desconto é de 5%. O Valor a Pagar é: R$ {:.2f}'.format(self.produto, desconto))
        elif self.forma_pagamento == 3:
            print('Olá você comprou um/a {}, com pagamento em 2x no cartão, O Valor a Pagar é: R$ {:.2f}'.format(self.produto, self.valor))
        elif self.forma_pagamento == 4:
            juros = (self.valor * 0.20) + self.valor
            print('Olá você comprou um/a {}, com pagamento em 3x ou mais, com juros de 20%. O Valor a Pagar é: R$ {:.2f}'.format(self.produto, juros))
        print(37 * '-=-')


def Opcoes():
    print('Opões de Pagamentos:')
    print('(1) - Ávista em dinheiro ou cheque desconto 10%')
    print('(2) - Cartão Avista desconto 5%')
    print('(3) - Cartão em 2x sem juros')
    print('(4) - Cartão em 3x ou mais 20%')


opcoes = Opcoes()
print(37 * '-=-')

item1 = Vendas(str(input('Digite o nome do produto: ')), float(input('Digite o valor R$: ')), int(input('Digite a opção de pagamento: ')))
item1.Pagamanto()
