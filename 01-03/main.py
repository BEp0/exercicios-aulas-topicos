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
    print(linha)
    print(f'{cores["amarelo"]}Atividade de Tópicos do dia 01/03!{cores["sem_cor"]}')
    print('Escolha a forma que quer realizar a operação:')
    print('[1] - Digitando o número do dia da semana \n (retorna o nome do dia)')
    print('[2] - Digitando o nome do dia da semana \n (retorna o número do dia)')
    escolha = str(input(f'{cores["amarelo"]}Qual você escolhe?'))

    while not (escolha == '1' or escolha == '2'):
        print(f'{cores["vermelho"]}ERRO!!! Digite de novo...{cores["sem_cor"]}')
        escolha = str(input('Qual você escolhe?'))

    if escolha == '1':
        digito.por_numero(escolha)
    else:
        nome.por_escrita(escolha)

if __name__ == "__main__":
    main()
