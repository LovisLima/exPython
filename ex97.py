# Faça um programa que tenha uma função chamada escreva(), que receba
# um texto qualquer como parãmetro e mostre uma mensagem
# com tamanho adaptável.

def escreva(msg):

    tam = len(msg) + 2
    print('-'*tam)
    print(f'{msg}')
    print('-'*tam)


#Programa Principal
msg = str(input('Digite algo: '))

escreva(msg)
