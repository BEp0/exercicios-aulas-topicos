def criarPHE():
    
    fonte = open('/home/souza/Documents/Programas-GitHub/Topicos-avancado/19-04/Entrega-Bernardo-Fenil/files-pdb/cadeiaA.pdb', 'r')
    destino = open( '/home/souza/Documents/Programas-GitHub/Topicos-avancado/19-04/Entrega-Bernardo-Fenil/files-pdb/fenil.pdb', 'w' )
    cont = 0
    
    for i in fonte:
        if ( i[17:20] == 'PHE'):
            if ( i[13:15] == 'CA'):
                    cont += 1 # conta quantos foram encontrados
                    destino.write(i)

    print(f'FORAM ENCONTRADOS {cont}') # retorna no terminal quantos foram encontrados

    destino.close()
    fonte.close()
    

def obtemCadeiaA():
    
    fonte = open('/home/souza/Documents/Programas-GitHub/Topicos-avancado/19-04/Entrega-Bernardo-Fenil/files-pdb/7kms.pdb', 'r')
    destino = open('/home/souza/Documents/Programas-GitHub/Topicos-avancado/19-04/Entrega-Bernardo-Fenil/files-pdb/cadeiaA.pdb', 'w' )

    for i in fonte:
        if ( i[:4] == 'ATOM' ):
            if ( i[21] == 'A'):
                destino.write(i)
    
    destino.close()
    fonte.close()

def main():

    obtemCadeiaA() 
    criarPHE()

if __name__ == '__main__':
    main()
