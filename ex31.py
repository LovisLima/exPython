# Desenvolva um programa que pergunte a distancia de uma viagem
# em km. Calcule o preço da passagem, cobrando R$0,50 por km
# para viagens de até 200km e 0,45 para viagens mais longas.

dist = float(input('Digite a distância da viagem em km: '))

if dist <= 200:
    p = dist * 0.50
    print('valor da passagem é {:.2f} reais' .format(p))
else:
    p2 = dist * 0.45
    print('valor da passagem é {:.2f} rearis' .format(p2))

