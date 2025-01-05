"""
Repeticoes
while(enquanto)
Executa uma acao enquanto uma condicao for verdadeira
loop infinito
"""
condicao = True

while condicao:
    nome = input('Qual seu nome: ')
    print(f'Seu nome e {nome}')

    if nome == 'sair':
        break

print('Acabou')