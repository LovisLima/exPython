#Faça a sequência de Fibonacci

print('Essa é uma sequencia de fibonacci')
n = int(input('Quantidade de termos que voce quer mostrar: '))
ultimo = 1
penultimo = 1

print('{}'.format(penultimo), end='')
if n==1 or n==2:
    print('1')
else:
    cont = 3
    while cont <= n:
        t = ultimo + penultimo
        penultimo = ultimo
        ultimo = t
        cont += 1
        print('->{}'.format(t),end='')
print('->FIM')





