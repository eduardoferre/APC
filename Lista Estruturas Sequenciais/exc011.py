def peso_ideal(alt):
    pi_hm = 72.7 * alt - 58.0
    pi_ml = 62.1 * alt - 44.7
    print(f'{pi_hm:.2f} {pi_ml:.2f}')

alt = float(input())
peso_ideal(alt)