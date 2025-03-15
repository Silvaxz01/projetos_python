"""
Concatenando e estendendo listas em python.

Listas em Python
Tipolist - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item ou indice escolhido
    pop - Remove do final ou indice escolhido
    del - Apaga um indice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_a.extend(lista_b)
print(lista_a)