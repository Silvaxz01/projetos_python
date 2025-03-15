"""
split e join com list e str
split - divide uma string
join - une uma string
strip - corta o espaco do comeco e do fim da string
"""
frase = 'Olha so que, coisa interessante'
lista_palavras = frase.split()

lista_frases = []
for i, frase in enumerate(lista_palavras):
    #print(lista_palavras[i].strip())
    lista_frases.append(lista_palavras[i].strip())

#print(lista_palavras)
frases_unidas = '-'.join(lista_frases)
print(frases_unidas)