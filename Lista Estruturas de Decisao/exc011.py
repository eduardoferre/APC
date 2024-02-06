def riscu(powerA, powerB):
    powerA = int(powerA)
    powerB = int(powerB)

    if powerA > powerB:
        print('Jogador A vence')

    elif powerA < powerB:
        print('Jogador B vence')

    elif powerA == powerB:
        print('Dois jogadores igualmente fracos')

riscu(5, 10)
riscu(1033, 999)
riscu(457278, 457278)
