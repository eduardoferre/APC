def print_rectangle(a):
    espacos = ' '*(a-2)
    print(a)
    print('+'*a)
    print(f'+{espacos}+')
    print('+'*a)


a, b, c = [int(i) for i in input().split()]
print_rectangle(a)
print_rectangle(b)
print_rectangle(c)