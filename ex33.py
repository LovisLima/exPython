# Faça um programa que leia tres números e mostre qual
# é o maior e qual é o menor

n1 = float(input('primeiro numero: '))
n2 = float(input('segundo numero: '))
n3 = float(input('terceiro numero: '))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

# Verificando quem é o maior

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor digitado foi', menor)
print('O maior valor digitado foi', maior)