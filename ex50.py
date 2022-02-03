# Desenvolva um programa que leia seis numeros inteiros e mostre a soma
# daqueles que forem pares se o valor digitador for impar desconsidere-o

soma = 0
for c in range(0,6):
    n = int(input('Digite o {}º numero: '. format(c)))
    if n % 2 == 0:
            soma += n
    elif n % 2 != 0:
        n = int(input('Digite novamente: '))

print (soma)


