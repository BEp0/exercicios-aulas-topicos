matriz = []


def inverter_linhas(linhas):
    lin1 = int(input('informe a primeira linha:'))
    lin2 = int(input('informe a segunda linha:'))
    for i in range(linhas):
        # deve ter o -1 para ser a unidade do user
        aux = matriz[i][lin1]
        matriz[i][lin1] = matriz[i][lin2]
        matriz[i][lin2] = aux


def multiplicar(linhas, colunas):
    fator = int(input('Digite o fator a multiplicar: '))
    for i in range(linhas):
        for j in range(colunas):
            if (i == j):
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0
            matriz[i][j] = matriz[i][j] * fator


def escrever(tipo):
    print(f'matriz: {tipo}')
    for i in matriz:
        print(i)


def inicializa(linhas, colunas):
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append("0")
        matriz.append(linha[:])


def main():
    linhas = int(input('Digite o número de linhas:'))
    colunas = int(input('Digite o número de colunas:'))
    inicializa(linhas, colunas)
    escrever('inicio')
    multiplicar(linhas, colunas)
    escrever('multiplicar')
    inverter_linhas(linhas)
    escrever('inverter linhas')


if __name__ == "__main__":
    main()
