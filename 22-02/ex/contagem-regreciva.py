from time import sleep


def contagem(tempo):
    if tempo == 0:
        print('\033[31mBOOM!\033[m')
    else:
        sleep(1)
        print(tempo)
        contagem(tempo - 1)


# deve executar
user_data = int(input('quantos segundos?'))
print(contagem(user_data))
