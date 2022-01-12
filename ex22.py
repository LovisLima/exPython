#len(frase)
#frase.count('o')
#frase.count('o', 0,13)
#frase.find('deo')
#frase.find('Android)
#'Curso' in frase

#Tranformação

#frase.replace('Python','Android')
#frase.upper()
#frase.lower()
#frase.capitalize()
#frase.title()
#frase.rstrip()
#frase.lstrip()

#Divisâo

#frase.split()

#Junção

#'-'.join(frase)


#frase = 'Curso em Video Python'
#dividido = frase.split()
#print(dividido[3])
#print(frase.split())

nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print ('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {}{}{} e ele tem {} letras'. format('\033[;31;40m',
                                                               separa[0],'\033[m', len(separa[0])))


