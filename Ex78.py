# Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
# posições na lista

maior = menor = 0
valores = []
for l in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {l}: ')))
    if  l == 0:
        maior = menor = valores[l]
    else:
        if valores[l] > maior:
            maior = valores[l]
        if valores[l] < menor:
            menor = valores[l]

print('=-'*30)
print(f'Voce digitou os valores {valores}')
print(f'Maior: {maior} nas posições ', end='')

for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print('')
print(f'Menor: {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')



# print(f'Menor: {menor} nas posições' )
# print(f'O maior valor digitado foi {max(valores)}, na posição {valores.index(max(valores))} ')
# print(f'O menor valor digitado foi {min(valores)}, na posição {valores.index(min(valores))}')
