# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista.Caso o némero já exista lá dentro, ele nao será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente

valores = []
N = ''
S = True
while True:
    v = (int(input(f'Digite um valor : ')))
    if v not in valores:
        valores.append(v)
        print('Adicionado com sucesso')
    else:
        print('Valor ja adicionado. Tente outro valor')

    p = str(input('Deseja continuar?: [S/N]')).strip().upper()[0]
    while p not in 'SN':
        p = str(input('Deseja continuar?: [S/N]')).strip().upper()[0]
    if p == 'N':
        break
valores.sort()
print(f'O valores digitados, em ordem crescente foraw: {valores}')


