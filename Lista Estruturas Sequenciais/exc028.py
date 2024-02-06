a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

a = a + a * 0.1
b = b + b * 0.1
c = c + c * 0.1
sm_tt = a + b + c

print(f'{a:.2f} {b:.2f} {c:.2f}')
print(f'{sm_tt:.2f}')