def somalista(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma


def main():
    v = input('Quantos vertices o grafo tem?')
    m = []
    l = []
    for i in range(int(v)):
        l.append(0)
    for i in range(int(v)):
        m.append(l[:])
    e = input('Quantas arestas o grafo tem?')
    for i in range(int(e)):
        o = input('Origem : ')
        d = input('Destino: ')
        oi = int(o)-1
        di = int(d)-1
        m[oi][di] = 1
        m[di][oi] = 1

    for i in m:
        print(i)
    print

    grau = somalista(m[0])

    for i in m:
        n = somalista(i)
        if n == grau:
            regular = True
        else:
            regular = False
    print
    if regular:
        print('O grafo é Regular!')
    else:
        print('O grafo não é Regular!')


main()
