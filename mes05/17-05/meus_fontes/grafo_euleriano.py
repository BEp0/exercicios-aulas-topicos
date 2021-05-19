'''Revisando Grafos'''


def somar(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma


def main():
    # receber a quantidade de vertices
    vertices = int(input('Quantidade de vertices: '))

    # criar duas listas
    m = []  # esta lista vai receber uma cópia da l
    l = []  # esta lista recebera o valor 0, aparecera N vezes, N == vertices

    # agora atribuimos 0 de acordo com a quantidade de vertices em l
    for i in range(vertices):
        l.append(0)  # adiciona a lista n zeros

    for i in range(vertices):
        m.append(l[:])  # cria uma cópia da lista anterior na lista m

    # verificar quantas arestas tem o grafo
    arestas = int(input('Quantidade de arestas: '))

    # adicionar a m a origem e o destino de cada aresta
    for i in range(arestas):
        # receber a origem e o destino
        origem = int(input('Origem: '))
        destino = int(input('Destino: '))

        # consiferam que se o usuário dizes que o 1 vai pro dois, na verdade é do 0 ao 1, por isso o -1:
        o_indice = origem - 1  # identificamos as posições de cada entrada e saída
        d_indice = destino - 1

        # criamos duas matriz, onde para a origem e destino recebem 1
        m[o_indice][d_indice] = 1  # o destino recebe 1
        m[d_indice][o_indice] = 1  # a origem recebe 1

    euleriano = True  # iniciamos como verdadeiro, caso não for par, mudamos dapois

    # percorremos, então, a lista m e atribuimos uma função somar com parametro i
    for i in m:
        print(i)  # mostramos como ficou o m
        # retorna a soma dos valores correspondentes as arestas de origem e saida anteriormente criados
        n = somar(i)
        if n % 2 != 0:  # a condição para ser euleriano é que os vertices sejam pares, logo se não forem não é euleriano
            euleriano = False

    # mostramos na tela se é ou não euleriano
    if euleriano:
        print('O grafo e Euleriano!')
    else:
        print('O grafo não e Euleriano!')


if __name__ == "__main__":
    main()
