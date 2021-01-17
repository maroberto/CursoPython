d = float(input('Quantp dinheiro você tem na carteira? R$ '))
dolar = float(5.10)
resultado = d / dolar
print('Com R${} você pode comprar US${:.2f}'.format(d, resultado))
