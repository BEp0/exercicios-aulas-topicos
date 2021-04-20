# exemplo de manipulação de arquivo dado pelo professor

def obtemCadeiaA():
    fonte = open('/home/souza/Documents/Programas-GitHub/Topicos-avancado/19-04/7kms.pdb', 'r')
    destino = open( '/home/souza/Documents/Programas-GitHub/Topicos-avancado/19-04/7kmsA.pdb', 'w' )
        
    for i in fonte:
        if ( i[:4] == 'ATOM' ):
            if ( i[21] == 'A'):
                destino.write(i)


    destino.close()
    fonte.close()


def main():
    obtemCadeiaA()


if __name__ == "__main__":
    main()