def classificador(a: int, b: int, c: int):
    if (a+b)>c and (a+c)> b and (b+c)>a:
        print('triangulo')
        
        if a!=b and a!=c and b!=c:
            print('escaleno')
        if a==c or a ==b:
            print('isosceles') 
        if a==b and a==c and b==c:
            print('equilatero')
        
        h = a
        c1 = b
        c2 = c
        if a>b and a>c:
            h = a
            c1 = b
            c2 =c
        elif b>a and b>c:
            h = b
            c1 = a
            c3 = c
        elif c>a and c>b:
            h = c
            c1 = a
            c2 = b
        
        if (h**2 == c1**2 + c2**2):
            print('retangulo')

    else:
        print('gondim sendo gondim')


classificador(3, 3, 3)
classificador(3,5,4)
