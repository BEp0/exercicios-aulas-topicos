def main():
    t = input( 'Escolha: 1-grafo 2-digrafo' ) 
    v = input( 'Quantos vertices o grafo tem?' )
    m = []
    l = []
    for i in range( int(v) ):
        l.append( 0 )
    for i in range( int(v) ):
        m.append( l[:] )
    e = input( 'Quantas arestas o grafo tem?' )
    for i in range( int(e)):
        o = input( 'Origem : ' )
        d = input( 'Destino: ' )
        oi = int(o)-1
        di = int(d)-1
        m[oi][di] = 1
        if int(t) == 1:
            m[di][oi] = 1
    for i in range( int(v) ):        
        print (m[i])
        print( "\n" )
    
main()
