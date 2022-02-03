# A confederação Nacional de natação precisa de um programa que leia o ano
#  de nascimento de um atleta e mostre a sua categoria de acorda com a idade:
# - até 9 anos : mirim
# - até 14 anos: infantil
# - até 19 anos junior
# - até 25 anos: sênior
# - acima: master

from datetime import date

atual = date.today().year
n = int(input('ano nascimento: '))
idade = atual - n
print ('O atleta tem {} anos.' .format(idade))
if idade <=9:
    print('Classifcacao: Mirim')
elif idade <= 14:
    print('Classificação Infantil')
elif idade <= 19:
    print('Classificaçao Junior')
elif idade <= 25:
    print ('Classificação Senior')
else:
    print ('Classificação master')




