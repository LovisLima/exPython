# Calculo de uma PA, com while (refazendo o exercicio 61)
# Pergunte ao usuário se ele quer mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos

print("Essa é uma progressao aritimética")

primeiro = int(input("Digite o primeiro termo da progressão: "))
r =  int(input("Razão: "))
termo = primeiro
cont = 1
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        cont += 1
        termo += r
        print ('{}'.format(termo), end =' ->')
    (print('PAUSA'))

    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados'.format(total))

