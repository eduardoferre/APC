days1, days2, days3 = input().split()
days1 = int(days1)
days2 = int(days2)
days3 = int(days3)


def age (days):
    a = days // 360
    m = (days%360)//30
    d = days%30

    print(f'{a} {m} {d}')

age(days1)
age(days2)
age(days3)