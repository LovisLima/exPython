#Crie um progarama que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda nao atingiram a maioridade
#e quantas ja sao maiores

from datetime import date

atual = date.today().year

totmaior = 0
totmenor = 0
for n in range (1,7):
    n = int(input('Digite o ano de nascimento: \n' ))
    idade = atual - n
    if idade > 18:
        totmaior += 1
        print( 'Essa pessoa tem {} anos, ela já atingiu a maioridade etária '.format(idade))
    else:
        totmenor += 1
        print('Essa pessoa tem {} anos, ela ainda não atingiu a maioridade etária '.format(idade))

print('Ao todo, tivemos {} pessoas maiores de idade e {} menores de idade'.format(totmenor, totmaior))