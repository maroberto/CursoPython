for i in range(0, 100):
    n = int(i)
    if (n > 1) and (n % n == 0) and (n % 1 == 0) and (n / n == 1) and\
       (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0) and (n % 7 != 0):
        print('É um número prinmo: {}'.format(n))
