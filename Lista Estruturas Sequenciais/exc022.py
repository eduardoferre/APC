def print_rectangle(a):
    espaco = ' ' * (a-2)
    print(a)
    print('x'*a)
    print(f'x{espaco}x')
    print(f'x{espaco}x')
    print('x'*a)

a, b, c = [int(i) for i in input().split()]
print_rectangle(a)
print_rectangle(b)
print_rectangle(c)
