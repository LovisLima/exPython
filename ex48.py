# Faça um programa que calcule a soma entre todos os numeros impares que sao
# multiplos de três e que se encontram no intervalo de 1 a 500

soma= 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0 :
        cont += 1
        soma += c
print('A soma dos {} valores solitados é {}'.format(cont,soma))



