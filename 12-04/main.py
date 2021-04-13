from random import randint


def main():

    d1 = randint(1, 6)  # dado 1
    d2 = randint(1, 6)  # dado 2
    soma = d1 + d2
    ponto = 0

    if soma == 7 or soma == 11:
        print('pass')

    elif soma == 2 or soma == 3 or soma == 12:
        print("don't pass")

    elif soma >= 4 and soma <= 10:
        ponto = soma

        while not soma == 7:
            # reatribui aos dados
            d1 = randint(1, 6)
            d2 = randint(1, 6)
            soma = d1 + d2

            if soma == 7:
                print("don't pass")

            elif soma == ponto:
                print('pass')
                break


if __name__ == "__main__":
    main()
