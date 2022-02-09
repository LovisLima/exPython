#Análise de dados em tupla
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
# uma tupla. No final mostre:
# Quantas vezes apareceu o valor 9
# Em que posição apareceu o primeiro valor 3
# Quais foram os numeros pares

cont=0
num = (int(input(" Digite um valor: ")),
      int(input(" Digite outro valor: ")),
      int(input(" Digite mais um valor: ")),
      int(input(" Digite o ultimo valor: ")))
print(f'Você digitou os valores {num}')
print(f'O numero nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero três apareceu na {num.index(3)+1}º posição')
else:
    print(' Nenhum numero 3 foi digitado')
print('Os valres pares digitados foram', end= ' ' )
for n in num:
    if n % 2 == 0:
        print(n,end= ' ' )

