# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$ 7,00 por cada km
# acima do limite

v = float(input('Digite a velocidade do carro: '))

if v > 80:
    m = 7 * (v-80)
    print('Voce foi multado no valor de R$ {:.2f} por execesso de velocidade'.format(m))

else:
    print('Você está dentro do limite de velocidade')