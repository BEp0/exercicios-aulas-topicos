'''
explicação:

'''

# Escolher pelo número:
def por_numero(dia_da_semana):

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

    print(f'O dia da semana é: {dia.capitalize()}')

# -----------------------------------------------------

# Escolher pelo nome:
def por_escrita(dia_da_semana):

    if dia_da_semana == 'SÁBADO' or dia_da_semana == 'DOMINGO':
        dia == 'fim de semana (sem número)'
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
        dia = 'Inválido'

    print(f'O número do dia da semana é: {dia}')
