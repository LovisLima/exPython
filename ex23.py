#dividir os caracteres de um numero , ler um numero de 0 a 9999
#e mostrar na tela cada um dos dígitos separados

num = int(input('Informe um número: '))
u = num // 1 %10
d = num // 10 %10
c = num // 100 %10
m = num // 1000 %10

print('Analisando o numero {}'. format(num))
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
