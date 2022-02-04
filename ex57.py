#Faça um programa que leia o sexo de uma pesso, mas só aceite os valores 'M'
#OU 'F'. Caso esteja errado, peça a digitação novamente até ver o valor correto


sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
 sexo = str(input('Dados inválidos.Por favor, informe seu sexo: ')).strip().upper()[0]
print('sexo {} resultado com sucesso'.format(sexo))
