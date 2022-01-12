# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente

fra = str(input('Digite uma frase: ')).strip()
separa = fra.split()
print(' Seu primeiro nome é {}{}{} '.format('\033[;31;40m',separa[0],'\033[m'))
print('Seu ultimo nome é {}{}{}'.format('\033[;31;40m',separa[-1],'\033[m'))




