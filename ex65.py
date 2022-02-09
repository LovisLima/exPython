# Ler varios numeros inteiros pelo teclado. No final da execução, mostre a
# media entre todos os valores e qual foi o maior e o menor valoers lidos. O programa
# deve perguntar ao usuário se ele quer ou nao continuar a digitar valores

resp ='S'
n = soma = cont = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n
    resp = str(input('Quer continuar? S/N ')).upper().strip()[0]
print('Acabou')
media = soma/cont
print(f'Você digitou {cont} numeros e a média foi {media} \n '
      f'O maior valor foi {maior} e o menor foi {menor} ')


