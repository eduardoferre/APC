def maravilhosos(x):
    x = int(x)

    if x == 1:
        print(x)

    elif x != 1:
        print(x)
        while x != 1:
            if x % 2 == 0:
                x = x / 2
                print(int(x))
            else:
                x = 3 * x + 1
                print(int(x))


x = int(input())
res = maravilhosos(x)