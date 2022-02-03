# Faça um programa que leia um numero inteiro
# e diga se ele é ou nao é primo


tot = 0
n = int (input(" Digite um numero: "))
for c in range (1, n + 1):
    if n % c == 0:
        print ('\033[34m', end = ' ')
        tot += 1
    else:
        print ('\033[m', end =' ')
    print('{}'. format(c), end = ' ')
print ('\n\033[m O numero {} foi divisivel {} vezes'. format(n, tot))

if tot > 2:
    print( " Esse numero não é primo")
elif tot == 2:
    print (" Esse numero é primo")
