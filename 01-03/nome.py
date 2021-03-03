# Escolher por dia (escrever o nome do dia da semana)
def por_escrita(dia_da_semana):
    if dia_da_semana == 'SEGUNDA':
        escolha = '2'
    elif dia_da_semana == 'TERÇA':
        escolha = '3'
    elif dia_da_semana == 'QUARTA':
        escolha = '4'
    elif dia_da_semana == 'QUINTA':
        escolha = '5'
    elif dia_da_semana == 'SEXTA':
        escolha = '6'
    elif dia_da_semana == 'SÁBADO' or dia_da_semana == 'DOMINGO':
        escolha == 'fim de semana'

    print(escolha)
