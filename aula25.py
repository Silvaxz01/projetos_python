"""
Formatacao de strings 
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
<- Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')