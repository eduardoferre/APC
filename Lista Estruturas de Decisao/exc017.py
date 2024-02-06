from calendar import c


def quantosJantam (n: int, g: int, f: int, c: int):
    total_par = min(g, f)
    total = total_par + c

    if n == 0:
        print('0')

    elif total <= n:
        print(total)

    elif total >= n:
        print(n)

   


quantosJantam(10, 3, 1, 4)
quantosJantam(15, 2, 5, 2)
quantosJantam(12, 0, 1, 7)
quantosJantam(10, 7, 5, 6)