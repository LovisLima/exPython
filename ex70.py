# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000,00
# Qual é nome do produto mais barato


menor = maior = cont = contP = preço = soma = 0

while True:
    print('-' * 20)
    print('CADASTRO DE PRODUTOS')
    print('-' * 20)
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço:R$ '))
    soma += preço
    cont += 1
    if preço > 1000:
       contP += 1

    if cont == 1 or preço < menor:
        menor = preço
        maior = preço

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if resp == 'N':
            break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total gasto na compra foi R${soma:.2f}')
print(f'Quantidade de produtos acima de R$1000,00: {contP}')
print(f'O produto com menor preço é R$ {menor:.2f}')