nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
        ...
else:
        print("Desculpe, voce deixou campos vazios")

if nome and idade:
    print(f'Seu nome e {nome} ')
    print(f'Seu nome invertido e {nome [::-1]}')
    print(f'Seu nome tem {len (nome)} letras')
    print(f'A primeira letra do seu nome e {nome[0]}' )
    print(f'A ultima letra do seu nome e {nome[-1]}' )
    if nome and idade:
        ...
    else:
        print("Desculpe, voce deixou campos vazios")
    if nome in " ":
        print('Seu nome tem espaco')
    else:
        print('Seu nome nao tem espaco')
