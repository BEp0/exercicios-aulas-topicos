'''
abrir um 3° arquivo 

abrir o destino

percorrer o destino e bravar no arquivo fenil

as linhas onde tenho um carbono CA e o aminoacido é PHE
'''


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
         