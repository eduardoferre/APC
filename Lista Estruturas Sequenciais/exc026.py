def vestimentas(x, y):
    m = 0
    
    if x > y:
        m = x - (x - y)

    else:
        m = y - (y - x)


    print(m * 2)

vestimentas(6, 9)