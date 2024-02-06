hora = str(input())

hh, mm, ss = int(hora[0:2]), int(hora[3:5]), int(hora[6:8])

hrs_em_segs = hh * 3600
ms_em_segs = mm * 60

total_segs = ss + hrs_em_segs + ms_em_segs

print(f'La se foram {total_segs} segundos que nao voltam mais...')
