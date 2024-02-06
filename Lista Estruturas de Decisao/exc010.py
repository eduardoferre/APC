def older(age1, age2):
    age1 = int(age1)
    age2 = int(age2)

    if age1 > age2:
        print('A')

    elif age1 < age2:
        print('B')

    elif age1 == age2:
        print('Maybe twins')

older(5, 10)
older(19, 17)
older(56, 56)