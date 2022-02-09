# Crie uma tupla unica com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços , organizando os dados em forma tabular

listagem = ('1apis', 3.30,
            'borracha',2.00,
            'apontador', 1.00,
            'estojo',10.00,
            'mochila',50.00)
print('-'*35)
print(f'{"Lista de Produtos":^30}')
print('-'*35)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
     print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R$ {listagem[pos]:.2f}')
print('-'*35)