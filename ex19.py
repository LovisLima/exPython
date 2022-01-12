from random import choice

aluno1 = str(input('Digite o primeiro aluno: '))
aluno2 = str(input('Digite o segundo aluno: '))
aluno3 = str(input('Digite o teceiro aluno: '))
aluno4 = str(input('Digite o quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'. format(escolhido))
