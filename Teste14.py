
n = int (input('Digite um numero para calcular seu Fatorial: '))
c = n
f=1
for c in range (5,0,-1):
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    f = f * c
    c -= 1
print('\n O fatorial de {} é {}.'.format(n, f))