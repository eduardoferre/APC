def pacotesDeBolacha (m, n, k):
    while n * k > m:
        k = k - 1
    total = n * k
    print(total)

pacotesDeBolacha(23,6,6)
