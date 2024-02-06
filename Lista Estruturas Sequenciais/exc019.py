def pacotesDeBolacha(m, n, k):
    while (n * k) > m:
        k = k - 1
    pacotes_restantes = m - (n * k)
    print(pacotes_restantes)


pacotesDeBolacha(18,6,4)
