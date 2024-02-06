def vestimentas(x, y):
    m = 0
    
    if x > y:
        m = x - (x - y)

    elif y > x:
        m = y - (y - x)

    elif x == y:
        m = x
    
    print(m)

vestimentas(18, 5)


def vestimentasa(x,y):
    print(min(x,y))

vestimentasa(6,9)