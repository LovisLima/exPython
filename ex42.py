# Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
# um de seus lados deve ser maior que o valor absoluto (módulo) da
# diferença dos outros dois lados e menor que a soma dos outros dois lados.
# Acrescente o recurso de mostrar que tipo de triangulo será formado:
# Equilátero: Todos os lados iguais
# Escaleno: todos os lados diferentes
# Isosceles: dois lados iguais



r1 = float(input('Digite um primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo')
    if r1 == r2 and r2 == r3:
        print('Esse triangulo é equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print ('Esse trinagulo é isosceles')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print ('Esse triangulo é escaleno')

else:
    print ('Os segmentos acima não podem formar triângulo')