def qualPeriodo(m,a,s):
    m = str(m)
    a = int(a)
    s = int(s)

    ano_entrada = int(m[0] + m[1])
    ano_entrada = 2000 + ano_entrada
    
    semestre_entrada = int(m[3])

    ano_dentro = a - ano_entrada

    periodo_dentro = (ano_dentro * 2) + (s - semestre_entrada) + 1

    print(periodo_dentro)

qualPeriodo(200012345,2020,0)
qualPeriodo(200054321,2020,1)
qualPeriodo(180134242,2020,0) 

