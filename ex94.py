galera = list()
pessoa = {}
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = str(input('idade: '))
    galera.append(pessoa.copy())
    while True:
        resp = str(input(f'Deseja Continuar(S/N)?: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N')
    if resp == 'N':
        break

print(galera)
