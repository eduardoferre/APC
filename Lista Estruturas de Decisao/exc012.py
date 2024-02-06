def jogadas(a: int, b: int):
    diferenca = abs(a - b)
    resto = diferenca % 10
    total = abs(diferenca // 10)

    jogadas = 0
    if resto == 0:
        jogadas = total
    
    else: 
        jogadas = total + 1

    print(jogadas)


jogadas(13,42)