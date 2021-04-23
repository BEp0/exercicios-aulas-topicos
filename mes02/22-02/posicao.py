# funcao -> posicao
def posicao(palavra):
    pos = palavra.find(letra)
    if pos != -1:
        pos += 1  # pra tirar o zero
    else:
        pos = 'Inexistente'  # caso não tenha a letra
    return pos


for palavras in range(1, 4):
    print('-=' * 5)
    palavra = str(input('Palavra a ser analisada:')).upper().strip()
    letra = str(input('Letra para encontrar a posição:')).upper().strip()
    print(f'A posição é: {posicao(palavra)}')
