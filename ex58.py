from random import randint

computador = randint(0,10)
print('\033[;31;40m-=- \033[m'*20)
print('Vou pensar em um numero entre 0 e 10. Tente adinhar qual é')
print('\033[;31;40m-=- \033[m'*20)

palpites = 0
n = int(input("Digite o seu palpite: "))
while n != computador:
    palpites += 1
    if n < computador:
        n = int(input(' É maior...Tente novamente...'))
    elif n > computador:
        n = int(input(' É menor...Tente novamente...'))

print('parabens vc acertou! Vc fez {} palpites até acertar. O numero que eu pensei '
      'foi o {}'.format(palpites+1,computador))
