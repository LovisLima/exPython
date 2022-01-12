from random import shuffle

aluno1 = str(input('Digite o primeiro aluno: '))
aluno2 = str(input('Digite o segundo aluno: '))
aluno3 = str(input('Digite o teceiro aluno: '))
aluno4 = str(input('Digite o quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)