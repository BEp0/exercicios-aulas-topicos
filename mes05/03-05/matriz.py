'''EXEMPLO DADO PELO PROFESSOR, adaptado por mim'''


def main():

    vertices = input('Quantos vertices o grafo tem?')

    m = []  # matriz
    l = []  # lista grafos

    for i in range(int(vertices)):
        l.append(0)

    for i in range(int(vertices)):
        m.append(l[:])  # copiar a lista l para m

    arestas = input('Quantas arestas o grafo tem?')

    for i in range(int(arestas)):
        o = input('Origem : ')
        d = input('Destino: ')
        oi = int(o) - 1  # presizamos usar o -1 pq inicia em zero
        di = int(d) - 1  # presizamos usar o -1 pq inicia em zero
        m[oi][di] = 1  # adiciona a linha na posição (oi, di) 1
        m[di][oi] = 1  # adiciona a linha na posição (di, oi) 1

    for i in range(int(vertices)):
        print(m[i])
        print("\n")


if __name__ == "__main__":
    main()
