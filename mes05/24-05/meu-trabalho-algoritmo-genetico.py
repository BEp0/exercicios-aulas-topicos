import random
import math


def somalista(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma
#!/usr/bin/env python
# -*- coding: utf-8 -*-


_POPULACAO = 1000
_CROMOSSOMO = 28
_CONDICAO_PARADA = 200
_MAXIMO_MUTACOES = 20
_ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ '
_INICIO = 'WDLMNLT DTJBKWIRZREZLMQCO PZ'
_ALVO = ['METHINKS IT IS LIKE A WEASEL',
         'METHINKS IT IS LIKE AN APPLE', 'IGUESS THAT IS LIKE A WEASEL']


def geraPopulacaoInicial():
    cromossomos = []
    for i in range(_POPULACAO):
        cromossomo = []
        for j in range(28):
            cromossomo.append(_INICIO[j])
        cromossomos.append(cromossomo[:])
    return cromossomos[:]

# Quanto mais letras mais adaptado


def calculaAdaptabilidade(populacao):
    '''
    pesquisar 3 frases, e a com maior indice será retornado
    '''
    indice = []
    for i in range(_POPULACAO):
        indice.append(0)

    for i in range(_POPULACAO):
        indiceElemento = 1
        for j in range(_CROMOSSOMO):
            if populacao[i][j] == _ALVO[0][j]:
                indiceElemento0 = indiceElemento+10
            if populacao[i][j] == _ALVO[1][j]:
                indiceElemento1 = indiceElemento+10
            if populacao[i][j] == _ALVO[2][j]:
                indiceElemento2 = indiceElemento+10
        if indiceElemento2 < indiceElemento0 > indiceElemento1:
            indice[i] = indiceElemento0
        if indiceElemento2 < indiceElemento1 > indiceElemento0:
            indice[i] = indiceElemento1
        if indiceElemento0 < indiceElemento2 > indiceElemento1:
            indice[i] = indiceElemento2

    return indice[:]


def mostraMelhorDaGeracao(condicaoParada, populacao, adaptabilidade):
    melhor = 0
    j = 0
    posicao = 0
    for i in adaptabilidade:
        if i > melhor:
            melhor = i
            posicao = j
        j = j + 1
    print("Melhor cromossomo " + str(posicao) + " da " +
          str(condicaoParada) + " geração, com indice = " + str(melhor))
    print(populacao[posicao])


def somaIndices(adaptabilidade):
    somatorio = 0
    for i in adaptabilidade:
        somatorio = somatorio + i
    return somatorio


def geraCrossingOver(populacao, adaptabilidade):
    soma = somaIndices(adaptabilidade)
    novaGeracao = []
    cruzamentos = _POPULACAO / 2
    for i in range(int(cruzamentos)):
        filhoA = []
        filhoB = []
        sorteioPai = int(math.floor(random.random() * soma))
        # pai
        indicePai = 0
        while (sorteioPai > 0):
            sorteioPai = sorteioPai - adaptabilidade[indicePai]
            indicePai = indicePai + 1
        indicePai = indicePai - 1
        if indicePai < 0:
            indicePai = 0
        indiceMae = indicePai
        while indiceMae == indicePai:
            sorteioMae = int(math.floor(random.random() * soma))
            # mae
            indiceMae = 0
            while (sorteioMae > 0):
                sorteioMae = sorteioMae - adaptabilidade[indiceMae]
                indiceMae = indiceMae + 1
            indiceMae = indiceMae - 1
            if indiceMae < 0:
                indiceMae = 0

        # Crossing over em si
        pai = populacao[indicePai][:]
        mae = populacao[indiceMae][:]

        pontoDeCrossing = 2+int(math.floor(random.random() * (_CROMOSSOMO-3)))
        for i in range(pontoDeCrossing):
            filhoA.append(pai[i])
            filhoB.append(mae[i])
        for i in range(pontoDeCrossing, _CROMOSSOMO):
            filhoA.append(mae[i])
            filhoB.append(pai[i])

        novaGeracao.append(filhoA[:])
        novaGeracao.append(filhoB[:])

    populacao = novaGeracao[:]


def geraMutacoes(populacao):
    quantidadeMutacoes = 20
    for i in range(quantidadeMutacoes):
        vitima = int(math.floor(random.random()*_POPULACAO))
        locusGene = int(math.floor(random.random()*_CROMOSSOMO))
        geneMutante = _ALFABETO[int(
            math.floor(random.random()*len(_ALFABETO)))]
        populacao[vitima][locusGene] = geneMutante

# Funcao principal


def main():

    condicaoParada = _CONDICAO_PARADA

    # Inicializo a minha população de cromossomos
    populacao = geraPopulacaoInicial()

    while (condicaoParada > 0):
        adaptabilidade = calculaAdaptabilidade(populacao)
#        print( adaptabilidade)
        mostraMelhorDaGeracao(condicaoParada, populacao, adaptabilidade)
        geraCrossingOver(populacao, adaptabilidade)
        geraMutacoes(populacao)
        condicaoParada = condicaoParada-1


if __name__ == '__main__':
    main()
