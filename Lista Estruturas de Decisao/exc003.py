def area(l, l1, forma):
    l = int(l)
    l1 = int(l1)

    if forma == 'retangulo':
        retangulo = l * l1
        print('O %s tem %i de area' % (forma, retangulo))

    elif forma == 'losango':
        losango = (l * l1) / 2
        print('O %s tem %i de area' % (forma, losango))

    elif forma == 'triangulo':
        triangulo = (l * l1) / 2
        print('O %s tem %i de area' % (forma, triangulo))

    elif forma == 'circulo':
        circulo = (pow(l, 2)) * l1
        print('O %s tem %i de area' % (forma, circulo))

area(10, 2, 'losango')
area(20, 4, 'retangulo')
area(15, 3, 'circulo')
area(72, 30, 'triangulo')