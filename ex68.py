# Faça um programa que jogue par ou impar com o computador. O jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo

print('-='*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*10)

from random import randint
computador = 0
v=0

while True:
    n = int(input('Digite um numero: '))
    computador = randint(0,10)
    total = n + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR?')).strip().upper()[0]
    print(f'Voce jogou {n} e o computador {computador}. Total é {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print(f'Você ganhou :) {total} é par!!')
            v += 1
        else:
            print(f'Você perdeu :( {total} é impar!!')
            print(f'Finalizando')
            break

    elif tipo =='I':
        if total % 2 != 0:
            print(f'Você ganhou :) {total} é impar!!')
            v += 1
        else:
            print(f'Você perdeu :( {total} é par!!')
            print(f'Finalizando')
            break
print(f'Game OVER! Você venceu {v} vezes.')

