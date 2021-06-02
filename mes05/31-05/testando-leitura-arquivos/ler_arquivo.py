arquivo = open("larinha.txt", "r")
escrever = open("larinha.txt", "a")

escrever.write('\nTe amo larinha!')
escrever.close()

for i in arquivo:
    print(i)

arquivo.close()
