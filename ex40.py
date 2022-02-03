#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# média abaixo de 5.0: reprovado
# média entre 5.0 e 6.0 recuperação
# média 7.0 ou superior: aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:  '))

media = (n1+n2)/2

if media < 5.0:
    print('Reprovado')
elif 7 > media >= 5.0:
    print('Recuperacao')
elif media >= 7:
    print('Aprovado')
