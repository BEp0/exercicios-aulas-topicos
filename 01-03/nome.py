# Escolher por dia (escrever o nome do dia da semana)
def por_escrita(escolha):
    escolha = str(input('Digite o dia da semana:')).upper()
    if escolha == 'SEGUNDA':
        escolha = '2'
    elif escolha == 'TERÇA':
        escolha = '3'
    elif escolha == 'QUARTA':
        escolha = '4'
    elif escolha == 'QUINTA':
        escolha = '5'
    elif escolha == 'SEXTA':
        escolha = '6'
    else:
        escolha == 'fim de semana'

    print(escolha)
