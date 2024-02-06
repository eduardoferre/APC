def sedeDeMelancia(w):
    w = int(w)
    res = w // 2

    if w % 2 == 0  and w != 2:
        print('SIM')

    else:
        print('NAO')

sedeDeMelancia(8)
sedeDeMelancia(15)
sedeDeMelancia(24)
sedeDeMelancia(10)
sedeDeMelancia(2)