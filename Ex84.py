# Faça um programa que leia o nome e peso de varias pessoas, guardando
# tudo em uma lista. No final mostre:
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas
# Uma listagem com as pessoas mais leves

lista = list()
dado = list()
men = mai = 0
while True:
    dado.append(str(input('Digite um nome: ')))
    dado.append(float(input('Digite um peso em kg: ')))
    if len(lista) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if  dado[1] < men:
            men = dado[1]
    lista.append(dado[:])
    dado.clear()
    p = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while p not in 'SN':
        p = str(input('Deseja continuar?: [S/N]')).strip().upper()[0]
    if p == 'N':
        break

print('-='*30)
print(f'Os dados foram {lista}')
print(f'Ao todo vc cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi {mai} kg Peso de ', end ='')
for p in lista:
    if p[1] == mai:
        print(f'({p[0]})', end ='')
print()
print(f'O menor peso é {men} kg')

