def area(l, l1, forma):
    l = int(l)
    l1 = int(l1)

    if forma == 'retangulo':
        retangulo = l * l1
        print("O %s tem %i de area" % (forma, retangulo))

    elif forma == 'losango':
        losango = (l * l1)/2
        print("O %s tem %i de area" % (forma, losango))


area(10, 2, 'retangulo')