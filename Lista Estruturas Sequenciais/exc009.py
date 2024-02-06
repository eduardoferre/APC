a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

def age(days):
    a = days // 360
    m = (days % 360) // 30
    d = days % 30
    print(f'{a} ano(s), {m} mes(es) e {d} dia(s)')

age(a)
age(b)
age(c)