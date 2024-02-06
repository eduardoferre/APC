import math

x, y = input().split()
x,y = [int(x) for x in input().split()]
x,y = map(int, input().split())

x = int(x)
y = int(y)

pot = math.pow(x, y)
print(pot)
