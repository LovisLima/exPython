# Crie um programa que leia dois valores e mostre um menu com operações
# aritiméticas. Seu programa deverá realizar a operaçao solicitada em cada caso

from time import sleep
opcao = 0
n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))


while opcao != 5:
    print('=-'*10)
    print('------ menu------ ')
    print('=-'*10)
    print('[1] somar\n'
          '[2] multiplicar\n'
          '[3] maior\n'
          '[4] novos numeros\n'
          '[5] sair do programa\n')

    opcao = int(input('Escolha uma opção do menu: '))

    if opcao == 1:
     print(" o valor da soma de {} e {} é {}".format(n1, n2, n1+n2))

    elif opcao == 2:
     print(" o valor da multiplicação de {} e {} é {}".format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior numero é {}'.format(n1))
        else:
            print('O maior numero é {}'.format(n2))
    elif opcao == 4:
        print('Informe os numeros novamente: ')

        n1 = float(input('primeiro numero: '))
        n2 = float(input('segundo numero: '))

    elif opcao == 5:
        print('Finalizando')
        print('=--'*10)
        sleep(1)
        print('Programa finalizado.Inicie novamente')

    else:
        print('Opção inválida. tente novamente')


