#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import sys
import os
import string
import random
import math

_POPULACAO       = 100
_CROMOSSOMO      = 10
_CONDICAO_PARADA = 200
_MAXIMO_MUTACOES = 10
_CONSOANTES      = 'bcdfghjklmnpqrstvxwyz'
_VOGAIS          = 'AEIOU'
_ALFABETO        = 'abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ0123456789'
_MAIUSCULAS      = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
_MINUSCULAS      = 'abcdefghijklmnopqrstuvxwyz'
_ALGARISMOS      = '0123456789'

def geraPopulacaoInicial():
    cromossomos = []
    for i in range(_POPULACAO):
        cromossomo = []
        for j in range( _CROMOSSOMO ):
            cromossomo.append( '_' )
        cromossomos.append( cromossomo[:] )
    cromossomos.append( 0 )
    return cromossomos[:]

# Quanto mais letras mais adaptado 
def calculaAdaptabilidade( populacao ):
    indice = []
    for i in range( _POPULACAO ):
        indice.append(0)

    for i in range( _POPULACAO ):
        indiceElemento = 1
        for j in range( (_CROMOSSOMO // 2) -1 ):
            if populacao[i][j] in _ALFABETO:
                indiceElemento = indiceElemento+10;
                indPalindromo = _CROMOSSOMO - j - 1
                if populacao[i][j] == populacao[i][indPalindromo]:
                    indiceElemento = indiceElemento+500
        indice[i] = indiceElemento
    return indice[:]

def mostraMelhorDaGeracao( condicaoParada, populacao, adaptabilidade ):
    melhor = 0
    j = 0
    posicao = 0
    for i in adaptabilidade:
        if i > melhor:
            melhor = i
            posicao = j  
        j = j + 1
    print( "Melhor cromossomo " + str( posicao ) + " da " + str( condicaoParada ) + " geração, com indice = " + str( melhor ) )
    print( populacao[posicao])

def somaIndices( adaptabilidade ):
    somatorio = 0
    for i in adaptabilidade:
        somatorio = somatorio + i
    return somatorio

def geraCrossingOver( populacao, adaptabilidade ):
    soma = somaIndices( adaptabilidade )
    novaGeracao = []
    cruzamentos = _POPULACAO / 2
    for i in range( int(cruzamentos) ):
        filhoA = []
        filhoB = []
        sorteioPai = int( math.floor( random.random() * soma ) )
        # pai
        indicePai = 0;
        while ( sorteioPai > 0 ):
            sorteioPai = sorteioPai - adaptabilidade[ indicePai ]
            indicePai = indicePai + 1
        indicePai = indicePai - 1
        if indicePai < 1:
            indicePai = 1
        indiceMae = indicePai
        while indiceMae == indicePai:
            sorteioMae = int( math.floor( random.random() * soma ) )
            # mae
            indiceMae = 0;
            while ( sorteioMae > 0 ):
                sorteioMae = sorteioMae - adaptabilidade[ indiceMae ]
                indiceMae = indiceMae + 1
            indiceMae = indiceMae - 1
            if indiceMae < 1:
                indiceMae = 1

        # Crossing over em si
        pai = populacao[ indicePai ]
        mae = populacao[ indiceMae ]

        pontoDeCrossing = 1+int( math.floor( random.random() * (_CROMOSSOMO-2 ) ) )
        for i in range( pontoDeCrossing ):
            filhoA.append( pai[i] )
            filhoB.append( mae[i] )    
        for i in range( pontoDeCrossing, _CROMOSSOMO ):
            filhoA.append( mae[i] )
            filhoB.append( pai[i] )    

        novaGeracao.append( filhoA[:] )
        novaGeracao.append( filhoB[:] )

    populacao = novaGeracao[:] 

def geraMutacoes( populacao ):
    quantidadeMutacoes = int( math.ceil( random.random()*_MAXIMO_MUTACOES ) ) 
    for i in range( quantidadeMutacoes ):
        vitima = int( math.floor( random.random()*_POPULACAO ) )
        locusGene = int( math.floor( random.random()*_CROMOSSOMO ) )
        geneMutante = _ALFABETO[int( math.floor( random.random()*len(_ALFABETO) ) )]
        populacao[vitima][locusGene] = geneMutante

# Funcao principal
def main():

    condicaoParada = _CONDICAO_PARADA

    # Inicializo a minha população de cromossomos
    populacao = geraPopulacaoInicial()

    while (condicaoParada>0):
        adaptabilidade = calculaAdaptabilidade(populacao)
        mostraMelhorDaGeracao( condicaoParada, populacao, adaptabilidade )
        geraCrossingOver( populacao, adaptabilidade )
        geraMutacoes( populacao )
        condicaoParada = condicaoParada-1


if __name__ == '__main__':
    main()

