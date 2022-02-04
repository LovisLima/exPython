# Crie um prorama que leia varios numeros inteiros pelo teclado,
# O programa só vai parar quando o usuário digitar o valor 999, que é
# a condição de parada. No final, mostre quantos numeros foram digitados e qual foi
# a soma entre eles (descondiderando a flag)

n = 0
soma = 0
cont = 0
while True:
    n = int(input('Digite um numero: '))
    if n==999:
        break
    soma += n
    cont += 1
    print(f'A soma dos numeros digitados foi {soma}:')
print(f'Voce digitou {cont} numeros')


