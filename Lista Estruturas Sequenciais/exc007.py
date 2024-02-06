def maiorAB(x, y):
    if x > y:
        print(x)

    elif x == y :
        print(x)
        
    else:
        print(y)

for i in range(5):
    x, y = [int(x) for x in input().split()]
    maiorAB(x, y)