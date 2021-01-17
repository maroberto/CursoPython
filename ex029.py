import random

velocidade = random.randint(60, 100)
multa = 7
valor_multa = (velocidade - 80) * multa


if velocidade <= 80:
    print('Você passou a {} kmh e está dentro do limite de velocidade!'.format(velocidade))
else:
    print('Você passou a {} Kmh e foi multado em R$: {:.2f}'.format(velocidade, valor_multa))
