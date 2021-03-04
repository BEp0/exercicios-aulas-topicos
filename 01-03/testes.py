
'''
    espaça para fazer testes para mandar na main
    por favor desconsidere este documento, é apenas para testar

'''


cores = {
    'sem_cor': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
}
linha = f'{cores["verde"]}-=-' * 36 + f'{cores["sem_cor"]}'
escolha_do_menu = ''
escolha_do_dia = ''
dia_da_semana = ''
dia = ''
# -----------------Escolher pelo número ------------


def por_numero(dia_da_semana):

    if dia_da_semana == '1' or dia_da_semana == '7':
        return dia_da_semana == 'fim de semana'

    elif dia_da_semana == '2':
        dia = 'segunda'
    elif dia_da_semana == '3':
        dia = 'terça'
    elif dia_da_semana == '4':
        dia = 'quarta'
    elif dia_da_semana == '5':
        dia = 'quinta'
    elif dia_da_semana == '6':
        dia = 'sexta'
    else:
        dia = 'inválido'

    while dia == 'inválido':
        print(f'{cores["vermelho"]}ERRO!!!{cores["sem_cor"]}')
        dia = ''
        escolha_do_dia = str(input('Digite novamente número do dia da semana:'))
        por_numero(escolha_do_dia)


def main():

    # ---------------MENU------------------------

    print(linha)
    print(
        f'{cores["vermelho"]}Atividade de Tópicos do dia 01/03!{cores["sem_cor"]}')
    print(linha)
    print(
        f'{cores["amarelo"]}Escolha uma das opções abaixo para realizar a operação:{cores["sem_cor"]}')
    print(f'{cores["amarelo"]}[1]{cores["sem_cor"]} - Nessa opção você deverá digitar o número do dia da semana e o programa te retornará o nome deste dia \n (Ex.: 2 ==> Segunda)')
    print(linha)

    escolha_do_menu = str(input('Digite aqui a sua escola [1 ou 2]:'))
    print(linha)
# --------- validação ----------------
    while not (escolha_do_menu == '1' or escolha_do_menu == '2'):
        print(f'{cores["vermelho"]}ERRO!!! Digite de novo...{cores["sem_cor"]}')
        escolha_do_menu = str(input('Digite aqui a sua escola [1 ou 2]:'))
        print(linha)
# ------operações---------------------
    if escolha_do_menu == '1':
        escolha_do_dia = str(input('Digite número do dia da semana:'))
        print(linha)
        por_numero(escolha_do_dia)

    print(dia_da_semana)
# --------final-----------------
    print(linha)
    print('__FIM__')
    print(linha)


if __name__ == "__main__":
    main()
