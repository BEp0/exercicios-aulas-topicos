
# jogo de dados

from random import randint
from time import sleep

def main():

    print(f'Jogando os dados...')

    sleep(1)

    # lança os dados a primeira vez
    d1 = randint(1, 6)  # dado 1
    d2 = randint(1, 6)  # dado 2
    soma = d1 + d2
    ponto = 0 # ponto usado caso a soma seja entre 10 > x > 4


    if soma == 7 or soma == 11:
        print(f'A soma deu {soma}')
        print('Pass')

    elif soma == 2 or soma == 3 or soma == 12:
        print(f'A soma deu {soma}')
        print("Don't pass")

    elif 10 > soma > 4:
        
        ponto = soma
        
        print(f'Seus pontos foram {ponto}')

        sleep(1)
        
        print('Jogando os dados novamente...')
        
        while not soma == 7:

            # relançar os dados
            d1 = randint(1, 6)
            d2 = randint(1, 6)
            soma = d1 + d2

            print(f'A nova pontuação foi: {soma}')

            sleep(1)

            if soma == 7:
                print("Don't pass")

            elif soma == ponto:
                print('Pass')
                break
    else:
        print('ERROR...')


if __name__ == "__main__":
    main()
