# Escolher por dia (escrever o nome do dia da semana)
def por_escrita():
    dia_semana = str(input('Digite o dia da semana:'))
    if dia_semana == '2':
        dia_semana = 'segunda'
    elif dia_semana == '3':
        dia_semana = 'terça'
    elif dia_semana == '4':
        dia_semana = 'quarta'
    elif dia_semana == '5':
        dia_semana = 'quinta'
    elif dia_semana == '6':
        dia_semana = 'sexta'
    else:
        dia_semana == 'fim de semana'
    print(dia_semana)
