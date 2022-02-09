#Crie um programa que tenha uma tupla totalmente preenchida com uma
#contagem por extenso, de zero até vinte
#Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e
#mostrá-lo por extenso

n = ('zero', 'um' , 'dois', 'tres', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze',
'quatorze','quinze','dezesseis','dezessete', 'dezoito','dezenove','vinte')



while True:

    ler = int (input('Digite um numero entre 0 e 20: '))
    if 0 <= ler <=20 :
        break
    print('Tente novamente', end='')
print(f'Voce digitou o numero {n[ler]}')
