# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
# No final do programa, mostre:
#
# A Média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

sIdade = 0
maiorIdadeHomem = 0
totMulher20 = 0
nomeVelho=''
NomeMulher=''
for p in range(1,5):

    print('------{}º PESSOA------'.format(p))
    nome = str(input('Digite o seu nome: '))
    idade = int (input('Digite a sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    sIdade += idade
    if idade == 1 and sexo in 'Mm':
     maiorIdadeHomem = idade
     nomeVelho = nome
     nomeMulher = nome
    elif idade > maiorIdadeHomem and sexo in 'Mm':
     maiorIdadeHomem = idade
     nomeVelho = nome
    elif idade < 20 and sexo in 'Ff':
     idadeMulher = idade
     totMulher20 += 1
     print('\n')
print('O Homem mais velho do grupo tem {} anos e se chama {}'.format(maiorIdadeHomem,nomeVelho))
print('A media de idade do grupo é de {} anos'.format(sIdade/p))
print('Existem {} mulheres com menos de 20 anos no grupo'.format(totMulher20))