# Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteio e somaPar(). A primeira
# função vai sortear 5 numeros e vai colocá-los dentro de uma lista
# e a segunda vai mostrar a soma entre todos os valores PARES
# sorteados pela função anterior


from random import randint
from time import sleep
def sorteio(lista):
    print('SORTEIO')
    for cont in range(0,5):
        n = randint(0,100)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteio(numeros)
somaPar(numeros)



