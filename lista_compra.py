"""
Faca uma lista de compra com listas
O usuario deve ter a possiblidade de
inseriri, apagar e listar valores da sua lista...
"""
import os
lista = []

while True:
    print('Selecione uma opcao')
    opcao = input('[i]inserir [a]apagar [l]listar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um numero inteiro.')
        except IndexError:
            print('Indice nao existe na lista.')
        except Exception:
            print('Erro desconhecido.')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l. ')