def formamisteriosa(a: int, b: int, c: int):
    
    if a == b:
        print('pode ser quadrado')

    elif a != b:
        print('pode ser retangulo')

    if (a+b)>c and (a+c)>b and (b+c)>a:
        if a==b and b==c and a==c:
            print('pode ser triangulo equilatero')
        elif a!=b and b!=c and a!=c:
            print('pode ser triangulo escaleno')
        elif a==b or a==c:
            print('pode ser triangulo isosceles')

formamisteriosa(3,5,4)
