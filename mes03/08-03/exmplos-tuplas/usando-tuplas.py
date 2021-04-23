# usando tuplas em python
# tuplas são imutáveis

'''

Anotações aula tuplas do curso em video...
terceiro mundo... tenho que fazer os outros exercícios

O QUE É UMA TUPLA?

# variável dupla:
	## variáveis simples:
    	lanche = hamburger # variável simples (o que já se sabia...)
	    lanche = suco # substitui o hamburger por suco...
    ## Como são vairaveis duplas?
	    ### existem 3 tipos / formas
	        - tuplas;
	        - listas;
	        - dicionários;

	## Tuplas:
	    print(lanche[2])
	    print(lanche[0:2]) # do zero até o dois, mas não mostra o 2
	    print(lanche[1:]) # começa do 1 até o fim
	    len(lanche) #quandos tem dentro

	"AS TUPLAS SÃO IMUTÀVEIS"

'''

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# lanche[1] = 'refrigerante' => erro... são imutáveis

print('-=' * 10)
print(lanche)
print(len(lanche))
print(lanche[0])
print(lanche[1:3])
print(lanche[:-2])

print(sorted(lanche)) # deixa em ordem, alfabética? / cria uma lista

# escrever mais bonitinho...
print('-=' * 10)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print("comi pra caramba!!!")

# outra forma de usar o for, mostra a posição
print('-=' * 10)
for cont in range(0, len(lanche)):
        print(cont) # escreve de 0 a 4
        print(lanche[cont]) # mostra o que ta dentro
print("comi pra caramba!!!")

# outra maneira, mostar a posição
print('-=' * 10)
for pos, comida in enumerate(lanche): # tanto dado quanto valor
    print(f'Eu vou comer {comida} na posição {pos}.')
print("comi pra caramba!!!")

# ---------------------------------------------------------------------------

print('-=' * 10)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # junta uma tupla com a outra, a ordem importa
print(a)
print(b)
print(c)
print(c.index(8)) # que posição está o 8
print(c.count(5))# quantas vezes aparece o 5
print('-=' * 10)

# ----------------------------------------------------------------------------------

pessoa = ('Bernardo', 18, 'M')
print(pessoa)
del(pessoa) # apaga a tupla inteira
print(pessoa)