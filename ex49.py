# Refaça o Ex9 mostrando a tabuada de um numero
# que o usuario escolher, só que agora utilizando
# um laço for

num = int (input('Digite um numero da tabuada: '))
for c in range(1,10):
    print('{} x {:2} = {}'.format(num,c, num*1))
