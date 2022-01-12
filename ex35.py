
# Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
# um de seus lados deve ser maior que o valor absoluto (módulo) da
# diferença dos outros dois lados e menor que a soma dos outros dois lados.

r1 = float(input('Digite um primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triangulo')
else:
    print ('Os segmentos acima não podem formar triângulo')