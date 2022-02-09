#Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma
#tupla. Depois disso, mostre a listagem de numeros gerados e tambem indique
#o menor e o maior valor que estão na tupla.

from random import randint

computador = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

for c in computador:
    print(f'{c} ', end='')
print(f'O maior valor sorteado foi {max(computador)}')
print(f'O menor valor sorteado foi {min(computador)}')