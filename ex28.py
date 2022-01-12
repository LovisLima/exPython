# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota '))
# m = (n1 + n2)/2
# print("A sua média foi {:.1f}". format(m))
# if m >= 6:
#    print('A sua média foi boa! PARABENS! ')
# else:
#    print("Sua média foi ruim")


# computador gerou um numero e 1 a 5 e o
# usuário precisa descobrir quye numero é esse

from random import randint

computador = randint(0, 5)
print('\033[;31;40m-=- \033[m'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('\033[;31;40m-=- \033[m'*20)
n = int(input("Digite um numero de 0 a 5: "))
if n == computador:
    print('Voce acertou!')
else:
    print('Eu pensei no numero {} e nao no numero {}'. format(computador,n))