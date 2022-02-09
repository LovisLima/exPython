#Analise de Dados do Grupo:
# Ler idade e sexo de várias pessoas. A cada pessoas cadastrada.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou nao
# continuar. No final mostre o total de pessoas com mais de 18 anos. O total de homens
# cadastrados e o total de mulheres com menos de 20 anos


contI = contH = contF = contF20 = contT= 0

resp = ' '
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo[M/F]: ')).strip().upper()
    contT += 1
    if idade > 18:
        contI += 1
    if sexo in 'M':
       contH += 1
    if sexo in 'F' and idade <20:
        contF20 +=1
    if sexo in 'F':
        contF += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Total de homens: {contH}')
print(f'Entre {contF} mulheres, {contF20} possuem menos de 20 anos')
print(f'Total de pessoas maiores de 18 anos: {contI}')