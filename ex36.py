#Escreva um programa que leia um numero inteiro qualquer e peça para o usuário
#escolher qual será a base de conversao

n = int( input("Digite um numero inteiro para conversao: "))
if (n >= 0):
    e = str(input('Digite binário, octal ou hexadecimal: '))
    if e == 'octal':
        print(oct(n)[2:])

    elif e == 'binário':
        print(bin(n)[2:])

    elif e == 'hexadecimal':
        print(hex(n)[2:])

    else:
        print("Opção invalida. Tente novamente")


else:
    print (" Digite um numero inteiro positivo")