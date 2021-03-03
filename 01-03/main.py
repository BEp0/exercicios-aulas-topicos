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
    
    escolha_do_menu = str(input('Qual você escolhe?'))
    print(linha)
    
    # ----- até aqui ok --------

    while not (escolha_do_menu == '1' or escolha_do_menu == '2'):
        print(f'{cores["vermelho"]}ERRO!!! Digite de novo...{cores["sem_cor"]}')
        escolha_do_menu = str(input('Qual você escolhe?'))

    if escolha_do_menu == '1':
        dia_da_semana = str(input('Digite o dia da semana:'))
        digito.por_numero(dia_da_semana)
    else:
        escolha_do_menu = str(input('Digite o dia da semana:')).upper()
        nome.por_escrita(dia_da_semana)

    print(escolha_do_menu)
    print(dia_da_semana)

if __name__ == "__main__":
    main()
