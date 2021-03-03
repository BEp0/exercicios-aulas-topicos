# Escolher por número
def por_numero(dia_da_semana):
    if dia_da_semana == '2':
        escolha = 'segunda'
    elif dia_da_semana == '3':
        escolha = 'terça'
    elif dia_da_semana == '4':
        escolha = 'quarta'
    elif dia_da_semana == '5':
        escolha = 'quinta'
    elif dia_da_semana == '6':
        escolha = 'sexta'
    elif dia_da_semana == '1' or dia_da_semana == '7':
        escolha == 'fim de semana'
    else:
        escolha == 'inválida'

    print(f'O dia da semana é: {escolha}')
