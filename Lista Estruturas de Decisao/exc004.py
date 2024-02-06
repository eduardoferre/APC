def banner (n: int):
    if n % 2 == 0 and n > 0:
        print('| | | | | | | | | |')

    elif n % 2 != 0 and n > 0:
        print('- - - - - - - - - -')

    elif n % 2 == 0 and n < 0:
        print('. . . . . . . . . .')

    elif n % 2 != 0 and n < 0:
        print('= = = = = = = = = =')

banner(-1)
banner(0)