import semanas_funcoes

cores = {
    'sem_cor':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}

linha = f'{cores["verde"]}-=' * 16 + f'{cores["sem_cor"]}'

escolha_do_menu = ''
escolha_do_dia = ''
dia_da_semana = ''
dia = ''

def main():

    print(linha)
    print(f'{cores["vermelho"]}Atividade de Tópicos do dia 01/03!{cores["sem_cor"]}')
    print(linha)
    print(f'{cores["amarelo"]}Escolha uma das opções abaixo para realizar a operação:{cores["sem_cor"]}')
    print(f'{cores["amarelo"]}[1]{cores["sem_cor"]} - Nessa opção você deverá digitar o número do dia da semana e o programa te retornará o nome deste dia \n (Ex.: 2 ==> Segunda)')
    print(f'{cores["amarelo"]}[2]{cores["sem_cor"]} - Nessa opção você deverá digitar o nome do dia da semana e o programa te retornará o número deste dia \n (Ex.: Segunda ==> 2)')
    print(linha)
    
    escolha_do_menu = str(input('Digite aqui a sua escola [1 ou 2]:'))
    print(linha)

    while not (escolha_do_menu == '1' or escolha_do_menu == '2'):
        print(f'{cores["vermelho"]}ERRO!!! Digite de novo...{cores["sem_cor"]}')
        escolha_do_menu = str(input('Digite aqui a sua escola [1 ou 2]:'))
        print(linha)

    if escolha_do_menu == '1':
        escolha_do_dia = str(input('Digite número do dia da semana:'))
        print(linha)
        semanas_funcoes.por_numero(escolha_do_dia)
    else:
        escolha_do_dia = str(input('Escreva o nome do dia da semana:')).upper()
        print(linha)
        semanas_funcoes.por_escrita(escolha_do_dia)
    
    print(linha)
    print('__FIM__')
    print(linha)

if __name__ == "__main__":
    main()
