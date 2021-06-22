# Voces podem melhorar este hash
def calculahash( a ):
    reshi = 0
    x = 1
    for i in a:
        reshi = reshi + (200-ord( i )) * x
        x = x + 1
    hash = reshi % 23    
    return hash    

def main():
    lista = []
    for i in range(0,23):
        lista.append(0)
    palavras = open('palavras.txt', 'r')
    for i in palavras:
        x = calculahash( i )
        print (i[0:-1] + '--' + str( x ))
        p = x
        inseriu = False
        while ( not inseriu ):
            if ( lista[ p ] == 0 ):
                lista[p] = i[0:-1]
                inseriu = True
            else:
                p = p + 1
                if ( p > 22 ):
                    p = 0
    print( 'Tabela hash preenchida:\n' )
    for i in lista:
        print( i )

if __name__ == '__main__':
    main()
        
