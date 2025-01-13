import os

palavra_secreta = 'pedra'
letras_acertadas = ''
tentativas = 0


while True:    
    letras = input(f'Digite uma letra para adivinhar a palavra  ')
    tentativas += 1

    if len(letras) > 1:
        print('Digite apenas uma letra.')
        continue

    if letras in palavra_secreta:
        letras_acertadas += letras

    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Plavra formada:', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCE GANHOU !! PARABENS !!!')
        print('A palavra era', palavra_secreta)
        print('Tentativas: ', tentativas)
        letras_acertadas = ''
        tentativas = 0
