matriz = []


def trocar_coluna(lin, col):
    col1 = int(input('informe a primeira coluna:'))
    col2 = int(input('informe a segunda coluna:'))
    for i in range(lin):
        aux = matriz[i][col1]
        matriz[i][col1] = matriz[i][col2]
        matriz[i][col2] = aux


def multiplicar(lin, col):
    fator = int(input('Informe o fatos:'))
    for i in range(lin):
        for j in range(col):
            matriz[i][j] = matriz[i][j] * fator


def dobra_linha(lin):
    linha = input('\nlinha que será dobrada:')
    l = int(linha) - 1
    for i in range(lin):
        matriz[l][i] = matriz[l][i]*2


def dobra_coluna(lin):
    coluna = input('\ncoluna que será dobrada:')
    cal = int(coluna) - 1
    for i in range(lin):
        matriz[i][cal] = matriz[i][cal]*2


def cria_matriz_identidade(lin, col):
    for i in range(lin):
        for j in range(col):
            matriz[i][j] = 1


def cria_matriz_diagonal_inversa(lin, col):
    max = col - 1  # -1 por causa que começa em 0
    for i in range(lin):
        for j in range(col):
            if (i == max - j):  # -1 para inverter
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0


def cria_matriz_diagonal(lin, col):
    for i in range(lin):
        for j in range(col):
            if (i == j):
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0


def imprime(mensagem):
    print(f'Matriz {mensagem}: \n')
    for i in matriz:
        print(i)


def inicializa(lin, col):
    for i in range(lin):
        linha = []
        for j in range(col):
            linha.append("0")
        matriz.append(linha[:])


def main():
    linhas = input("linhas: ")
    colunas = input("colunas")
    lin = int(linhas)
    col = int(colunas)

    inicializa(lin, col)
    imprime("inicio")
    cria_matriz_diagonal(lin, col)
    imprime("diagonal")
    cria_matriz_diagonal_inversa(lin, col)
    imprime("diagonal inversa")
    cria_matriz_identidade(lin, col)
    imprime("identidade")
    dobra_coluna(lin)
    imprime("dobra_coluna")
    dobra_linha(lin)
    imprime("dobra_linha")
    multiplicar(lin, col)
    imprime("multiplicar")
    trocar_coluna(lin, col)
    imprime("trocar colunas")


if __name__ == '__main__':
    main()
