import PySimpleGUI as sg


class TelaFina:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Qual o valor do imovel? R$: ', size=(27, 0)),
             sg.Input(size=(10, 1), key='saldo_devedor')],
            [sg.Text('Qual é a sua renda? R$: ', size=(27, 0)),
             sg.Input(size=(10, 1), key='salario')],
            [sg.Text('Em quantos anos quer pagar? ', size=(27, 0)),
             sg.Input(size=(10, 1), key='anos')],
            [sg.Output(size=(30, 20))],
            [sg.Button('Enviar Dados')]

        ]

        # Janela
        self.janela = sg.Window('Simulador de Financiamento').layout(layout)

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            saldo_devedor = self.values['saldo_devedor']
            salario = self.values['salario']
            anos = self.values['anos']
            print(f'saldo devedor R$: {saldo_devedor}')
            print(f'salario R$: {salario}')
            print(f'anos:  {anos}')
            #meses = anos * 12
            #valor_mes = saldo_devedor / meses
            # print(f'{meses}')
            # print(f'{valor_mes}')


tela = TelaFina()
tela.Iniciar()
