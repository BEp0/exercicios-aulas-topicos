# Voces podem melhorar este hash
def calculahash(a, posicoes):
    reshi = 0
    x = 2
    for i in a:
        reshi = reshi + (200-ord(i)) * x
        x = x + 3
    hash = reshi % posicoes
    return hash


def main():
    lista = []
    posicoes = 50
    for i in range(0, posicoes):
        lista.append(0)
    palavras = open('c:/temp/palavras2.txt', 'r')
    for i in palavras:
        x = calculahash(i, posicoes)
        print(i[0:-1] + '--' + str(x))
        p = x
        inseriu = False
        while (not inseriu):
            if (lista[p] == 0):
                lista[p] = i[0:-1]
                inseriu = True
            else:
                p = p + 1
                if (p > posicoes - 1):
                    p = 0
    print('Tabela hash preenchida:\n')
    for i in lista:
        print(i)


if __name__ == '__main__':
    main()
