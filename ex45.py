from random import randint

itens =('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('\033[;31;40m-=- \033[m'*20)
print('Vou pensar Em PEDRA, PAPEL ou TESOURA. Tente GANHAR...')
print('\033[;31;40m-=- \033[m'*20)

print ('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')


jog = int (input('Qual a sua jogada?'))
print('--=='*10)
print('O jogador escolheu {}' .format(itens[jog]))
print('O computador escolheu {} '.format(itens[computador]))
print('--=='*10)


if computador == 0 : # computador jogou PEDRA
    if jog == 0 : #PEDRA
        print ( 'empate')
    elif jog == 1: #PAPEL
        print ('jogador ganhou: papel cobre pedra')
    elif jog == 2: #TESOURA
        print ('jogador perdeu: pedra quebra tesoura')
    else:
        print('jogada invalida')
elif computador == 1 : # computador jogou PAPEL
        if jog == 0:  # PEDRA
            print('COMPUTADOR GANHOU: papel cobre pedra')
        elif jog == 1:  # PAPEL
            print('EMPATE')
        elif jog == 2:  # TESOURA
            print('JOGADOR GANHOUu: tesoura corta papel')
        else:
            print('jogada invalida')

elif computador == 2 : # computador jogou TESOURA
    if jog == 0:  # PEDRA
        print('JOGADOR GANHOU: pedra quebra tesoura')
    elif jog == 1:  # PAPEL
        print('COMPUTADOR GANHOU: tesoura corta papel')
    elif jog == 2:  # TESOURA
        print('empate')
    else:
        print('jogada invalida')


