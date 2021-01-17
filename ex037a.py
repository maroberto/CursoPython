saldo_devedor = float(200000)
taxa = float(0.0799)
anos = 25
parcelas = anos * 12
juros = (anos * taxa) / (parcelas)
amortizacao = saldo_devedor / parcelas


print('{:.2f}'.format(saldo_devedor*juros))
print('{:.2f}'.format(amortizacao))

for parcela in range(parcelas):
    saldo_devedor = (saldo_devedor - amortizacao)
    juros_mes = (saldo_devedor * juros)
    pagamento = (juros_mes + amortizacao)

    print(
        parcela, '{:.2f} / {:.2f} / {:.2f} / {:.2f}'.format(saldo_devedor, juros_mes, amortizacao, pagamento))
