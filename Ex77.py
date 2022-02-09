# Verificar as vogais existentes dentro de uma lista de palavras
palavra = ('1apis',
            'borracha',
            'apontador',
            'estojo',
            'mochila',)

for p in palavra:
    print(f'\n Na palavra {p} temos as vogais: ', end='')
    for letra in p:
       if letra in 'aeiouAEIOU':
           print(f'{letra}',end='')
# print(listagem)
# print(vogais)

