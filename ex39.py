#Faça um programa que leia o ano de nascimento de um jovem e informa,
# de acordo com sua idade , sel ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se já passou do tempo do tempo (alistamento)
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

atual = date.today().year
n = int(input(" Ano de nascimento: "))
idade = atual - n

if idade < 18:
    saldo = 18 - idade
    print('ele ainda vai se alistar ao serviço militar: faltam {} anos para se alistar'.format(saldo))
    ano = atual + saldo
    print ('vc vai se alistar em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print ('já passaram {} anos do tempo do tempo (alistamento)'.format(saldo))
    ano = atual - saldo
    print('Voce se alistou em {}'.format(ano))

elif atual - n == 18:
    print ("está no tempo de se alistar!")