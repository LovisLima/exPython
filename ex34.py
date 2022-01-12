# Escreva um programa que pergunte o salario de um funcionario
# e calcule o seu aumento. para salários
# superiores a R$ 1250,00, calcule um aumento de 10%
# Para inferiores ou iguais, o aumento é de 15 %

sal = float(input('Digite o seu salário: '))

if sal > 1250:
    print("O valor do seu aumento é de {:.2f} e o seu novo "
          "salário é {:.2f}".format(sal*0.1, sal*1.1))

else:
    print("O valor do seu aumento é de {:.2f} e o seu novo "
          "salário é {:.2f}". format(sal*0.15, sal*1.15))