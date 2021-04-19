
# jogo de dados

from random import randint
from time import sleep

def main():

    # lança os dados a primeira vez
    d1 = randint(1, 6)  # dado 1
    d2 = randint(1, 6)  # dado 2
    soma = d1 + d2
    ponto = soma # ponto usado caso a soma seja entre 10 > x > 4
    
    print(f'Jogando os dados...\n')
    print(f'Primeiro dado: \033[34m{d1}\033[m')
    print(f'Segundo dado: \033[34m{d2}\033[m')
    
    sleep(1)

    if soma == 7 or soma == 11:
        print(f'\nSeus pontos foram \033[32m{ponto}')
        sleep(1)
        print('Pass\033[m\n')

    elif soma == 2 or soma == 3 or soma == 12:
        print(f'\nSeus pontos foram \033[31m{ponto}')
        print("Don't pass\033[m\n")

    elif 10 >= soma >= 4:

        print(f'\nSeus pontos foram \033[32m{ponto}\033[m')

        sleep(1)
        
        print('\nJogando os dados novamente...')
        print('    Condições:')
        print('        - Se cair \033[31m7\033[m => o jogo ganha')
        print(f'        - Se cair \033[32m{ponto}\033[m => você ganha')
        print('\n\033[34mJogue até sair um dos números acima\033[m\n')
        
        sleep(2)

        while not soma == 7:

            # relançar os dados
            d1 = randint(1, 6)
            d2 = randint(1, 6)
            soma = d1 + d2

            print(f'A nova pontuação foi: {soma}')

            sleep(1)

            if soma == 7:
                print("\n\033[31m Don't pass \033[m\n")

            elif soma == ponto:
                print('\n\033[32m Pass \033[m\n')
                break
    else:
        print(soma, ponto)
        print('\033[31mERROR...\033[m')


if __name__ == "__main__":
    main()
