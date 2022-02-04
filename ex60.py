# Faça um programa que leia um numero qualquer e mostre o seu fatorial

n = int (input('Digite um numero para calcular seu Fatorial: '))
c = n
f = 1
print ('Calculando {}! = '.format((n), end=''))
while c > 0:
    print('{}'.format(c), end ='')
    print('x' if c > 1 else '=', end = '' )
    f = f * c
    c -= 1
print('O fatorial de {} é {}.'.format(n,f))