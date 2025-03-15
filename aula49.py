"""
Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
"""
lista_a = ['Luiz', 'Maria', 1]
lista_b = lista_a.copy()

lista_a[0] = 'qualquer coisa'
print(lista_a)
print(lista_b)