def chapeu(nome):
    cont = 0
    for i in nome:
        
        if nome[cont] == 'G':
                return print(nome, 'é da Grifinória')
        elif nome[cont] == 'S':
                return print(nome, 'é da Soncerina')
        elif nome[cont] == 'C':
                return print(nome, 'é da Corvinal')
        elif nome[cont] == 'L':
                return print(nome, 'é da Lufa-Lufa')

        cont += 1
    return print(nome, 'é da Grifinória')


def main():
    nome = input('digite o nome:').upper().strip()
    chapeu(nome)


if __name__ == "__main__":
    main()
