#numeros impares e pares, try e except no lugar de if e else funcionam tb.

entrada = input('Digite um numero: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'Impar'

    if par_impar:
        par_impar_texto= 'par'

    print(f'O numero {entrada_int} e {par_impar_texto}')
else:
    print('Voce na digitou um numero inteiro')