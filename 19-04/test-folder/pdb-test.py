'''
abrir um 3° arquivo 

abrir o destino

percorrer o destino e bravar no arquivo fenil

as linhas onde tenho um carbono CA e o aminoacido é PHE
'''


def obtemCadeiaA():
    
    fonte = open('/home/souza/Documents/Programas-GitHub/Topicos-avancado/19-04/7kms.pdb', 'r')
    destino = open( '/home/souza/Documents/Programas-GitHub/Topicos-avancado/19-04/test-folder/fenil-test.pdb', 'w' )
    
    for i in fonte:
        if ( i[:4] == 'ATOM' ):
            if ( i[21] == 'A'):
                if ( i[17:20] == 'PHE'):
                    if ( i[13:15] == 'CA'):
                        destino.write(i)

    destino.close()
    fonte.close()
    
'''
def criarphe():
    fonte = open('/home/souza/Documents/Programas-GitHub/Topicos-avancado/19-04/7kms.pdb', 'r')
    destino = open('/home/souza/Documents/Programas-GitHub/Topicos-avancado/19-04/fenil.pdb', 'w')

    for i in fonte:
        if ( i[:4] == 'ATOM' ):
            if ( i[21] == 'A'):
                if (i[:21] == 'PHE'):
                    if (i[:16] == 'CA'):
                        destino.write(i)

    destino.close()
    fonte.close()
'''


def main():

    obtemCadeiaA() 
    #criarphe()

if __name__ == '__main__':
    main()
         