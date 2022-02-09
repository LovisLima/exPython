# Fazer a Tabuada. Versao 3.0.
# O programa deve ser interrompido apenas quando o numero solicitado foi negativo

from time import sleep
cont = 0

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        print('Finalizando', end='')
        print('.',end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.',end='')
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Programa Finalizado')
