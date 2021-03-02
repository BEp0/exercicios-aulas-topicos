import digito
import nome

cores = {
    'sem_cor':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}

linha = f'{cores["verde"]}-=' * 16 + f'{cores["sem_cor"]}'


def main():
    # ------------------------
    print(linha)
    print(f'{cores["vermelho"]}Atividade de Tópicos do dia 01/03!{cores["sem_cor"]}')
    print(linha)
    print(f'{cores["amarelo"]}Escolha a forma que quer realizar a operação:{cores["sem_cor"]}')
    print(f'{cores["amarelo"]}[1]{cores["sem_cor"]} - Digitando o número do dia da semana \n (retorna o nome do dia)')
    print(f'{cores["amarelo"]}[2]{cores["sem_cor"]} - Digitando o nome do dia da semana \n (retorna o número do dia)')
    print(linha)
    # ----- até aqui ok --------
    escolha = str(input(f'{cores["amarelo"]}Qual você escolhe?')) # colorindo tudo

    while not (escolha == '1' or escolha == '2'):
        print(f'{cores["vermelho"]}ERRO!!! Digite de novo...{cores["sem_cor"]}')
        escolha = str(input('Qual você escolhe?'))

    if escolha == '1':
        digito.por_numero(escolha)
    else:
        nome.por_escrita(escolha)

if __name__ == "__main__":
    main()
