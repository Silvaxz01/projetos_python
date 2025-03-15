"""
Listas de listas e seus indices
"""
salas = [
    #0        1
    ['Pedro', 'Gabriela', ], #0
    #0
    ['Leite', ],  #1
    #0        #1        #2
    ['Henrique', 'Heitor', 'Dudis', ],  #2
]

#print(salas[0][1])
#print(salas[2][2])
#print(salas[2][3][2])

for sala in salas:
    print(f'A sala e {sala}')
    for aluno in sala:
        print(aluno)