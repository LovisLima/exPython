# Ler varios numeros e colocar em uma lista. Depois, criar duas listas extras
# que vao conter apenas valores pares e os valores impares digitados respectivamente.
# Ao final mostre o conteúdo das três listas geradas respectivamente
pares = list()
num = list()
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    p = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while p not in 'SN':
        p = str(input('Deseja continuar?: [S/N]')).strip().upper()[0]
    if p == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(num)
print(pares)
print(impares)
