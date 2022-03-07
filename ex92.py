# Crie um programa que leia, ano de nascimento e carteira de
# trabalho; casdastre-o em um dicionario.Se por acaso a CTPS for
# diferente de ZERO, o dicionario receberá tambem o ano de
# contratação e o salário.Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = {}
dados['nome']=str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year-nasc
dados['ctps'] = int(input('Carteira de Trabalho(0 não tem): '))
print(dados)
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação '))
    dados['salário'] = float(input('Salário:R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação']+35) - datetime.now().year)
print('=-' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')


E