'''
explicação:
    A função "por_numero" pede o numero para o usuário, dentro de 1 a 7. se não for neste intervalo de tempo e repete a operação para que ela seja realizada novamente. Assim, ela retorna o nome desse dia relativo ao número. Ex.: 2 ==> Segunda; 3 ==> Terça ...

    Já a outra, "por_escrita", recebe o nome do dia da semana e converte para o respectivo número, sendo a operação inversa da anterior. Ex.: Segunda ==> 2; Terça ==> 3 ...
'''

cores = {
    'sem_cor':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}

linha = f'{cores["verde"]}-=-' * 36 + f'{cores["sem_cor"]}'


# ------Escolher pelo número ------------

def por_numero(dia_da_semana):

# --------classificação---------------

    if dia_da_semana == '1' or dia_da_semana == '7':
        dia = 'fim de semana'
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

# -----------------------------------

# -------- mostrar a classificação/resultado ------

    print(linha)
    print(f'O dia da semana é: {cores["amarelo"]}{dia.capitalize()}{cores["sem_cor"]}')

# ---------------------------------------------

# --------validação------------------------

    while dia == 'inválido':
        print(linha)
        print(f'{cores["vermelho"]}ERRO!!!{cores["sem_cor"]}')
        dia = ''
        escolha_do_dia = str(input('Digite novamente número do dia da semana:'))
        por_numero(escolha_do_dia)

# -----------Encaminha para o fim-----------------------


# -----Escolher pelo nome:------------
def por_escrita(dia_da_semana):

# --------classificação---------------

    if dia_da_semana == 'SÁBADO' or dia_da_semana == 'DOMINGO':
        dia = 'fim de semana (sem número)'
    elif dia_da_semana == 'SEGUNDA':
        dia = '2'
    elif dia_da_semana == 'TERÇA':
        dia = '3'
    elif dia_da_semana == 'QUARTA':
        dia = '4'
    elif dia_da_semana == 'QUINTA':
        dia = '5'
    elif dia_da_semana == 'SEXTA':
        dia = '6'
    else:
        dia = 'inválido'

# -----------------------------------

    print(linha)
    print(f'O número do dia da semana é: {cores["amarelo"]}{dia}{cores["sem_cor"]}')

# ---------------------------------------------

# --------validação------------------------

    while dia == 'inválido':
        print(linha)
        print(f'{cores["vermelho"]}ERRO!!!{cores["sem_cor"]}')
        dia = ''
        escolha_do_dia = str(input('Dia inválido!!! \nEscrava novamente o nome do dia da semana:')).upper()
        por_escrita(escolha_do_dia)

# -----------Encaminha para o fim-----------------------
