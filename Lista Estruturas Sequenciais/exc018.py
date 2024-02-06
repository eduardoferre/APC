str1, str2, a = input().split()
a = int(a)

print(f'{str1}{str2}')
print(str1*a)
print((str1+str2)*a)


def concatenar(c1, c2):
    print(c1 + c2)

def repetir(c, num):
    print(c * int(num))

def ambos(c1, c2, num):
    c = c1 + c2
    print(c * int(num))

a, b, c = input().split()

concatenar(a, b)
repetir(a, c)
ambos(a, b, c)