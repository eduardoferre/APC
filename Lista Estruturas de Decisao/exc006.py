def dominos(n: int, m: int):
    tabuleiro = n * m

    if tabuleiro%2 == 0:
        result = tabuleiro/2
        print(int(result))

    else: 
        result = tabuleiro//2
        print(int(result))

dominos(2, 4)
dominos(3,3)
dominos(1,5)