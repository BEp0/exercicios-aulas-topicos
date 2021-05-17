'''EXEMPLO DADO PELO PROFESSOR, adaptado por mim'''


def main():

    tipo = input('Escolha: 1-grafo 2-digrafo')
    quantidade_vertices = input('Quantos vertices o grafo tem?')
    
    lista_adjacencia = []

    for i in range(int(quantidade_vertices)):

        m = []
        vertice = i+1
        m.append(vertice)
        m.append([])
        # copia a lista m para a lista "lista_adjacencia"
        lista_adjacencia.append(m[:])

    print(lista_adjacencia)  # mostra a lista zerada

    arestas = input('Quantas arestas o grafo tem?')

    for i in range(int(arestas)):

        o = input('Origem : ')
        d = input('Destino: ')
        oi = int(o)-1  # origem inteito - 1
        di = int(d)-1  # destino inteito - 1
        lista_adjacencia[oi][1].append(int(d))

        if tipo == '1':
            lista_adjacencia[di][1].append(int(o))

    for i in range(int(quantidade_vertices)):
        print(lista_adjacencia[i])


if __name__ == "__main__":
    main()
