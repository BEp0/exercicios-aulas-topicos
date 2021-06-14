def difere(x):
    for i in x:
        if(x[i] != x[0]):
            return True
    return False


def main():
    arquivo = open("Arquivo.txt")  # variável recebe o arquivo
    matriz_adjacencia = []  # aqui será feita a matriz adjacencia
    linhas = []  # aqui é as linhas para matriz anterior
    arvores_separadas = []  # criamos as arvores separadas
    tree = []  # criamos um spanning tree

    '''
    Agora faremos 2 coisas:
       1º construir a matriz de adjacencia
       2º iniciar a matris tree zerada para a resposta no futuro
    vamos lá:
    '''
    c = 0  # para não ter lixo
    for j in arquivo:
        c = c + 1  # nesse ponto temos que verificar se o c é 1, 2 ou != dos dois anteriores
        '''
        O que faremos agora:
        caso c == 1: vamos fazer 4 for's
            1º para criar um vetor com cada elemento do número de vertice
            2º para criar um vetor em linhas com zeros do tamanho do número de vertices
            3º para criar uma matriz adjacencia com cada linha copiada de linhas
            4º para criar a spanning tree também com cópias das linhas

        caso c == 2:
            vamos criar uma variavelque vai guardar a posição do j

        se não:
            vamos criar a matriz adjacente
        '''
        if c == 1:
            v = j  # v vai receber o valor j do for

            for i in range(int(v)):
                # criando elementos com a quantidade de vertice
                arvores_separadas.append(i)
            for i in range(int(v)):
                linhas.append(0)  # iniciando com zero
            for i in range(int(v)):
                # clonando as linhas para matriz adjacencia
                matriz_adjacencia.append(l[:])
            for i in range(int(v)):
                tree.append(l[:])  # clonando as linhas para a spanning tree
        elif c == 2:
            flag = j  # uma variável recebe a posição
        else:
            k = j.split()
            origem = k[0]
            destino = k[1]
            ponteiro = k[2]
            origem_int = int(origem)
            destino_int = int(destino)
            matriz_adjacencia[origem_int][destino_int] = int(ponteiro)
            matriz_adjacencia[destino_int][origem_int] = int(ponteiro)

        ''' Agora vamos imprimir a matriz e a arvore separada'''
        for i in range(int(v)):
            print(matriz_adjacencia[i])  # matriz adjacencia

        # arvore separada
        print(f'\n{a}\n')

        '''
        Agora vamos implementar o algoritmo de PRIM
        '''
    while(difere(a)):
        menorAresta = 10000  # dizemos que a menor aresta é um número muito alto
        # definimos a linha e a coluna como -1, pq começa em 0
        linha = -1
        coluna = -1
        for i in range(int(v)):  # para cada vertice
            for j in range(i + 1, int(v)):
                # i + 1 para começar em 1 ao invés de 0
                if matriz_adjacencia[i][j] != 0:
                    # o elemento não pode ser zero, logo, existe uma aresta entre i e j
                    if tree[i][j] == 0:  # não há aresta entre i e j na spanning tree
                        # validar se a aresta é menor
                        if matriz_adjacencia[i][j] < menorAresta:
                            if arvores_separadas[i] != arvores_separadas[j]:
                                menorAresta = matriz_adjacencia[i][j]
                                coluna = j
        # ao fim da validação (com o for) adicionamos a menor aresta na spanning tree
        tree[linha][coluna] = menorAresta
        '''após isso, devemos unificar as arvores, para isso, devemos saber qual tem o menore número, assim armazenamos o menor e maior valor em variáveis'''
        if arvores_separadas[linha] < arvores_separadas[coluna]:
            menor = arvores_separadas[linha]
            maior = arvores_separadas[coluna]
        else:
            maior = arvores_separadas[linha]
            menor = arvores_separadas[coluna]
        # agora vamos unificar os grupos usando um for
        for i in range(0, len(arvores_separadas)):
            if arvores_separadas[i] == maior:
                arvores_separadas[i] = menor
        print(arvores_separadas)
        print(f"Menor aresta: {menorAresta} \nLinha: {linha}\nColuna: {coluna}")
        # agora imprimimos a matriz tree como resposta
        for i in range(int(v)):
            print(tree[i])
        print('\n')


if __name__ == "__main__":
    main()
