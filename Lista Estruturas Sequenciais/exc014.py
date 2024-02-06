def quantosSemestres(m,a,s):
    m = str(m)
    a = int(a)
    s = int(s)

    ano_entrada = int(m[0] + m[1])
    ano_entrada = 2000 + ano_entrada
    
    semestre_entrada = int(m[3])

    ano_dentro = a - ano_entrada

    semestre_dentro = (s - semestre_entrada) + (ano_dentro * 2)

    print(semestre_dentro)

quantosSemestres(200012345,2022,0)