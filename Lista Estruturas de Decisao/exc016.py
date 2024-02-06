def piscininha(x, y, w, h, a, b):
    if (a > x) and (a < w + x) and (b > y) and (b < y + h):
        print('Dando um tchibum')

    elif (a < x) or (a > w + x) or (b < y) or (b > y + h):
        print('Tomando um solzin')
        
    else:
        print('So com os pezin dentro da agua')
       


piscininha(0, 0, 10, 10, 1, 1)
piscininha(0, 0, 10, 10, 0, 5)
piscininha(-10, -15, 5, 4, 0, 0)
