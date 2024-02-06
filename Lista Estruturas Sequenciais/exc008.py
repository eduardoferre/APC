def trocarAB(x, y):
    print(y, x)

for i in range(5):
    x, y = [int(x) for x in input().split()]
    trocarAB(x, y)