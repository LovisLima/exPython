# Ler varios numeros inteiros. Digitar a condição de parada: '999'.
# Mostrar quanto snumeros foram digitados e qual foi a soma entre eles
# (desconsiderando a flag)

n = soma = cont = 0
while True:
    n = int(input('Digite um numero: '))
    if n==999:
        break
    soma += n
    cont += 1
    print(f'A soma dos numeros digitados foi {soma}:')
print(f'Voce digitou {cont} numeros')