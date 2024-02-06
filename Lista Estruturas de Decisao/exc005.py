def dinheiros(n, a, b):
    galao_2l = (n//2) * b + (n%2 * a)
    galao_1l = n * a
    
    if n == 1:
        res =  0 + a
        print(res)
        
    elif galao_2l > galao_1l:
        print(galao_1l)

    elif galao_2l <= galao_1l:
        print(galao_2l)

dinheiros(1, 400, 3)
dinheiros(3, 1, 3)
dinheiros(7, 3, 2)