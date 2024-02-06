def ritmoMedio (h, m, s, p):
    horas_em_segundos = h * 3600
    minutos_em_segundos = m * 60
    segundos_totais = s + horas_em_segundos + minutos_em_segundos
    
    segundos_por_km = segundos_totais / p

    ritmo_min = segundos_por_km // 60
    ritmo_seg = segundos_por_km % 60

    ritmo_min, ritmo_seg = [int(i) for i in [ritmo_min, ritmo_seg]]
    if ritmo_min < 10:
        ritmo_min = f'0{ritmo_min}'
    if ritmo_seg < 10:
        ritmo_seg = f'0{ritmo_seg}'

    print(f'{ritmo_min}:{ritmo_seg} min/km')


ritmoMedio(4,32,57,48.1)