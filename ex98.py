# Faça um programa que tenha uma função chamada contador()
# , que receba três parãmetros: inicio,fin e passo. Seu programa
# tem que realizar três contagens através da função criada:
# a) de 1 a até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) Uma contagem personalizada
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p=1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.0)
    if i < f:
        cont = i
        print(f'-' * 30)
        while cont <= f:
            print(f' {cont} ', end='')
            cont += p
            sleep(0.5)
        print('')
        print(f'-' * 30)
        print('FIM')
    else:
        cont = i
        print(f'-' * 30)
        while cont >= f:
            print(f' {cont} ', end='')
            cont -= p
            sleep(0.5)
        print('')
        print(f'-' * 30)
        print('FIM')

#Programa principal
contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de fazer a contagem!')
print(f'-' * 30)
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)