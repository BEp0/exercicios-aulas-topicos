'''EXEMPLO DADO PELO PROFESSOR'''


def main():

    t = input('Escolha: 1-grafo 2-digrafo')
    v = input('Quantos vertices o grafo tem?')

    m = []
    l = []

    for i in range(int(v)):
        l.append(0)
    for i in range(int(v)):
        m.append(l[:])  # copia l em m

    e = input('Quantas arestas o grafo tem?')

    for i in range(int(e)):
        o = input('Origem : ')
        d = input('Destino: ')
        oi = int(o) - 1  # -1 devido ao inicio do range que é em zero
        di = int(d) - 1  # -1 devido ao inicio do range que é em zero

        m[oi][di] = 1

        if int(t) == 1:  # devido a opção digrafo, verificamos se é 1º ou 2º opção
            m[di][oi] = 1

    for i in range(int(v)):
        print(m[i])
        print("\n")


if __name__ == "__main__":
    main()
