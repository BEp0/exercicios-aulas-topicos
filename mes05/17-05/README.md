# Grafos:

Um grafo é a relação entro objetos de um determinado conjunto. Onde é chamadas de grafos G(V, E) onde V é o vértices e E é a Arestas (um subconjunto de paraes não ordenados de V).
- Vértices são os "pontinhos" dos grafos.
- Arestas são as linhas que ligam esses pontos.

Se E vai para V, dizemos que E é adjacente a V, ou vizinho também.

## Caminho:

As arestas que ligam um vértice a outro, ou liga uma sequência de vértices, é chamado de caminho.
    
- (v1, v2, v3, v4) => Liga de v1 a v4.
Logo, (v1, v2, v3) é um subcaminho do anterior.

### Comprimento do caminho:

- Quantidade de arestas do caminho

## Ciclo:

> Sai de um vértice e volta para o mesmo.

Em Grafos Dirigidos o ciclo deve ter ao menos uma aresta

Em Grafos Não Dirigidos o ciclo deve ter ao menos 3 arestas

### Tipos de ciclos:
- Cíclico = Tem ao menos um ciclo
- Acíclico = Não há ciclo

## Grafos Dirigidos;

> As arestas tem uma direção, relações com sentido definido.

Podemos pensar nas arestas como pares ordenados.

O par de vértices pode sair dele e chegar nele, self loop.

Grau é a soma das arestas que entram e que saem.

Grau de saída: os que saem do vértice.
Grau de entrada: os que entram no vértice.

- Fortemente conexo = Sempre que vai, volta
- Conexo = Vai mas pode não volta
- Fracamente conexo = Não ta quebrado, mas tem mais problemas
        
## Grafos Não Dirigidos:
> Não há a direção definida, logo o que sai de A para B vai também de B para A.

São pares não ordenados de vértices. E, não podem haver self loops.
(A, B) <=> (B, A).

Grau de Vértices = quantidade de arestas no vértices.

Conexo se cada par de vertice tiver um caminho