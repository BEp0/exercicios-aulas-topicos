def difere( x ):
    for i in x:
        if (x[i] != x[0]):
            return True
    return False    

def main():
    arq = open( 'c:\\temp\\grafo_mst.txt' )
    m = [] # matriz de adjacencia
    l = [] # para preencher as linhas
    a = [] # arvores separadas
    t = [] # spamming tree
    c=0
    for j in arq:
        c = c + 1
        if c == 1:
            v = j
            for i in range( int(v) ):
                a.append( i )
            for i in range( int(v) ):
                l.append( 0 )
            for i in range( int(v) ):
                m.append( l[:] )
            for i in range( int(v) ):
                t.append( l[:] )
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
    for i in range( int(v) ):
        print (m[i])    
    print( '\n')
    print( a )
    print( '\n')
    
    # Algoritmo de PRIM
    while ( difere( a ) ):
        menorAresta = 10000
        linha = -1
        coluna = -1
        for i in range( int(v) ):
            for j in range( i+1, int(v) ):
                if (m[i][j] != 0):
                    if (t[i][j] == 0 ):
                        if ( m[i][j] < menorAresta ):
                            if ( a[i] != a[j] ):
                                menorAresta = m[i][j]
                                linha = i
                                coluna = j
        t[linha][coluna] = menorAresta
        if ( a[linha]<a[coluna] ):
            z = a[linha]
            w = a[coluna]
        else:
            w = a[linha]
            z = a[coluna]
        for i in range( 0, len(a)):
            if (a[i] == w ):
                a[i] = z
        print( a )
        print( "Menor aresta: " + str( menorAresta ) + " " + str( linha ) + " " + str( coluna ) )

    for i in range( int(v) ):
        print (t[i])    
    print( '\n')
                
                
        
main()
