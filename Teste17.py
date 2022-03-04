pessoas = {'nome':'Gustavo','sexo':'M','idade':'22'}
pessoas['nome']='Leandro'
print(f"{pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.keys())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')