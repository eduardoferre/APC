
def resto (a, b, d):
    soma = a + b
    resto = soma % d
    print(resto)

for i in range(3):
    a, b, d = [int(i) for i in input().split()]
    resto(a, b, d)