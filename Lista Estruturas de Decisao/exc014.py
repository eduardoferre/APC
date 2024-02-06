def qtdcopos(n: int):
    
    if n == 0:
        print('Pode voltar pro ceubinho, deivis! Falta(m) 4 copo(s)!')

    elif n % 4 == 0:
        print('Pode levar pros calourinhos, deivis!')

    elif n % 4 != 0:
        cont = 0
        while n % 4 != 0:
            n += 1    
            cont += 1
        print(f'Pode voltar pro ceubinho, deivis! Falta(m) {cont} copo(s)!')
        
qtdcopos(0)
qtdcopos(8)
qtdcopos(7)
