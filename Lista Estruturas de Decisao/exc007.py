def realidade(a, b, c):
    delta = (pow(b, 2)) - 4 * a * c

    if delta == 0:
        print('reais')

    elif delta > 0:
        print('reais')

    elif delta < 0:
        print('complexas')

realidade(1, 0, -1)
realidade(1, 0, 1)
realidade(2, 4, 2)