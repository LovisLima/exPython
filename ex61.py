# Calculo de uma PA, com while (refazendo o exercicio 51)

# An = A1 + (n-1) * r

print("Essa é uma progressao aritimética")

primeiro = int(input("Digite o primeiro termo da progressão: "))
r =  int(input("Razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    cont += 1
    termo += r
    print ('{}'.format(termo), end =' ->')
(print('fim'))
