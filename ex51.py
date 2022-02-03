# Escreva uma PA: Leia o primeiro termo e a razao.
# Mostre os 10 primeiros termos dessa progressao

# An = A1 + (n-1) * r


print("Essa é uma progressao aritimética")

a1 = int(input("Digite o primeiro termo da progressão: "))
r =  int(input("Razão: "))
decimo = a1 + (10-1) * r
for c in range (a1,decimo + r ,r):
    print ('{}'.format(c), end =' ->')
(print('fim'))
