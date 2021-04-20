def obtemCadeiaA():
    
    fonte = open( '7kms.pdb', 'r' ) #caminhos inventados, muda de acordo com a maquina
    destino = open( '7kmsA.pdb', 'w' )
    
    for i in fonte:
        if ( i[:4] == 'ATOM' ):
            if ( i[21] == 'A'):
                destino.write(i)


    destino.close()
    fonte.close()

def main():

    obtemCadeiaA() 


if __name__ == '__main__':
    main()
         