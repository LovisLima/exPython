from math import sin, cos, radians
an = float(input('Digite o angulo que vc deseja: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
print('O angulo de {} tem o seno de {:.2f}'. format(an, seno))
print('O angulo de {} tem o cosseno de {:.2f}'. format(an, cosseno))