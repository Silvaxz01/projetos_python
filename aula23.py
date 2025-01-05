#Operadores in e not in
# Strings sao iteraveis
#  0 1 2 3 4 
#  P e d r o
# -5-4-3-2-1
#nome   = 'Pedro'

#print('dro' in nome)
#print('zero' in nome)
#print(10 * '-')
#print('dro' not in nome)
#print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')