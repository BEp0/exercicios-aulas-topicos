# Escolher por número
def por_numero(escolha):
    escolha = str(input('Digite o dia da semana:'))
    if escolha == '2':
        escolha = 'segunda'
    elif escolha == '3':
        escolha = 'terça'
    elif escolha == '4':
        escolha = 'quarta'
    elif escolha == '5':
        escolha = 'quinta'
    elif escolha == '6':
        escolha = 'sexta'
    else:
        escolha == 'fim de semana'

    print(escolha)
