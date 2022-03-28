def par(n=0):
    if n%2==0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par(num):
    print('Esse numero é Par')
else:
    print('Esse numero é Impar')