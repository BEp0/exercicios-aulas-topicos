# Esta funcao recebe uma lista x.
# e percorre a lista elemento por elemento.
# cada elemento i é comparado com o primeiro elemento.
# se pelo menos um for diferente retornará True.
# só retornará False quando todos os elementos forem iguais entre si.
def difere( x ):
    for i in x:
        if (x[i] != x[0]): # comparo aqui cada elemento com o primeiro elemento
            return True
    return False    

def main():
    arq = open( 'c:\\temp\\grafo_mst.txt' )
    m = [] # matriz de adjacencia
    l = [] # para preencher as linhas
    a = [] # arvores separadas
    t = [] # spamming tree

    #--------------------------------------------------------------------------------------------
    # Este trecho do programa constroi a matriz de adjacencia m
    # Este trecho tambem inicializa uma matriz t zerada para servir como resposta no futuro 
    c=0
    for j in arq:
        c = c + 1
        if c == 1:
            v = j
            for i in range( int(v) ):
                a.append( i )          # cria um vetor a com cada elemento sendo o numero do vertice
            for i in range( int(v) ):
                l.append( 0 )          # cria um vetor l com 0s do tamanho do numero de vertices
            for i in range( int(v) ):
                m.append( l[:] )       # cria uma matriz m com cada linha sendo uma cópia de l     
            for i in range( int(v) ):
                t.append( l[:] )       # cria uma matriz t com cada linha sendo uma cópia de l 
                                       # esta matriz t será a nossa Minimum Spanning Tree     
        elif c == 2:
            e = j
        else:
            k = j.split()
            o = k[0]
            d = k[1]
            p = k[2]
            oi = int(o)-1
            di = int(d)-1
            m[oi][di] = int(p)
            m[di][oi] = int(p)    
    #--------------------------------------------------------------------------------------------

    for i in range( int(v) ):
        print (m[i])               # imprime a matriz m
    print( '\n')
    print( a )                     # imprime o vetor de vertices
    print( '\n')
    #--------------------------------------------------------------------------------------------

    
    # Algoritmo de PRIM
    while ( difere( a ) ):  # enquanto existem arvores diferentes eu vou ficar neste enquanto
        menorAresta = 10000 # começo dizendo que a menor aresta é um numero muito grande
        linha = -1
        coluna = -1
        for i in range( int(v) ): # faço para cada vertice 
                                  # (para 7 vertices vou percorrer de 0 a 6, por exemplo )

            for j in range( i+1, int(v) ): # agora percorro de i+1 até 6. logo, na primeira 
                                           # vez, com i=0 eu vou de 1 a 6
                                           # na segunda volta vou de 2 a 6
                                           # na terceira volta vou de 3 a 6
                                           # na quarta volta vou de 4 a 6...
                                           # na ultima volta vou de 6 a 6

                if (m[i][j] != 0):         # se o elemento da matriz nao é zero (ou seja, 
                                           # se existe uma aresta entre i e j

                    if (t[i][j] == 0 ):    # se NAO existe uma aresta entre i e j na 
                                           # Matriz da Minimum Spanning Tree 

                        if ( m[i][j] < menorAresta ): # se a aresta m[i][j] é menor que
                                                      # a menor atual
                                                      # eu troco a menor atual para m[i][j]
                                                      # guardo a linha e a coluna da menor
                            if ( a[i] != a[j] ):
                                menorAresta = m[i][j]
                                linha = i
                                coluna = j

        # Depois de acabar o for eu identifiquei a menor aresta válida (nao forma circulos)
        # Então eu insiro esta menor aresta na minha solução, ou seja
        # insiro na Matriz de Adjacencias t 
        t[linha][coluna] = menorAresta

        # Agora vou unificar as arvores
        # Então eu primeiro descubro qual dentre elas tem o numero menor
        # o numero menor eu armazeno em z
        # o maior eu armazendo em w    
        if ( a[linha]<a[coluna] ):
            z = a[linha]
            w = a[coluna]
        else:
            w = a[linha]
            z = a[coluna]

        # agora que eu sei o numero menor z
        # troco todos os numeros que forem iguais a w 
        # para z por exemplo:
        # supondo que meu vetor a seja [0, 1, 1, 2, 3, 3, 4]
        # meu z seja 1
        # meu w seja 3
        # então percorro o vetor a trocando todos os 3 por 1
        # [0, 1, 1, 2, 3, 3, 4]
        #              ^  ^
        #              |  |
        #             troco 
        #             estes
        #             por 1    
        # ficando...
        # [0, 1, 1, 2, 1, 1, 4]
        #
        # unificando assim os grupos 1 e 3 transformando num unico grupo 1
        for i in range( 0, len(a)):
            if (a[i] == w ):
                a[i] = z
        print( a )
        print( "Menor aresta: " + str( menorAresta ) + " " + str( linha ) + " " + str( coluna ) )


    # Quando no vetor a ficarem todos os grupos iguais (todos 0)
    # o algoritmo terá preenchido a matriz t com a Minimum Spanning Tree
    # AGora eu imprimo a matriz t como resposta
    for i in range( int(v) ):
        print (t[i])    
    print( '\n')
                
                
        
main()
