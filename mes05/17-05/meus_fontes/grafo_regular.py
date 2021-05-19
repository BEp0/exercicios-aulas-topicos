def somar(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma


def main():
    # recebemos a quantidade de vertices e criamos as listas
    vertices = int(input('Vértices: '))
    m = []
    l = []

    for i in range(vertices):
        l.append(0)  # iniciar tudo com zero
    for i in range(vertices):
        m.append(l[:])  # adicionar (copyar) a lista l na m

    # recebe a quantidade de arestas
    arestas = int(input('Arestas: '))

    for i in range(arestas):
        # receber origem e destino
        origem = int(input('Origem: '))
        destino = int(input('Destino: '))

        # origem e destino real para o vetor
        o_indice = origem - 1
        d_indice = destino - 1

        # transforma a lista m em uma matriz, onde (A, B) = 1 e (B, A) = 1
        # o primeiro [] indica a lista que estamos e o segundo o lugar desta lista
        m[o_indice][d_indice] = 1
        m[d_indice][o_indice] = 1

    # vai somar os elementos da primeira lista dentro da lista m
    grau = somar(m[0])

    for i in m:  # percorremos a lista criada
        print(i)  # mostrar a lista
        n = somar(i)  # somamos todas os elementos dentro de cada lista da m
        if n == grau:  # caso a soma atual de == a soma anterior pelo primeiro elemento
            regular = True
        else:
            regular = False

    if regular:
        print('É Regular!')
    else:
        print('Não é Regular!')


if __name__ == "__main__":
    main()
