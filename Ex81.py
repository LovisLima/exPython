# Crie um programa para ler vários números e coolocar em uma lista. Depois disso, mostre:
# Quantos números foram digitados
# A lista de valores, ordenada de forma decrescente
# Se o valor 5 foi digitado e está ou não na lista

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    p =str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while p not in 'SN':
        p = str(input('Deseja continuar?: [S/N]')).strip().upper()[0]
    if p == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} valores')
print(f'Lista em ordem crescente: {lista}')
if 5 in lista:
    print(f'O numero 5 cinco está na lista')