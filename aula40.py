""" while/else
Se tiver um "break" no meio do whilw o else
nao sera executado .
"""
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1

else:
    print('O else foi executado.')