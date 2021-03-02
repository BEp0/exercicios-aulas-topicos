import digito
import nome

def main():
    print('Atividade de Tópicos!')
    print('Escolha a forma que quer realizar a operação:')
    print('[1] - Digitando o número do dia da semana')
    print('[2] - Digitando o nome do dia da semana')
    escolha = str(input('Qual você escolhe?'))

    while not (escolha == '1' or escolha == '2'):
        print('ERRO!!! Digite de novo...')
        escolha = str(input('Qual você escolhe?'))

    if escolha == '1':
        digito.por_numero()
    else:
        nome.por_escrita()

if __name__ == "__main__":
    main()