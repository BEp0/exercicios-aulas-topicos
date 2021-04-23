'''
romanos = {}
romanos['I']= 1
romanos['II'] = 2
print(romanos)'''

texto = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
texto += "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

lista = texto.split()

#print(list(texto)) => lista todas as letras
#print(lista)
#print(texto)
dicionario = {}
for i in lista:
    #percorrer palavra por palavra
    if i in dicionario:
        dicionario[i] += 1
    else:
        dicionario[i] = 1
for i in dicionario:
    print(i, dicionario[i])