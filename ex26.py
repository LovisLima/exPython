# Ler uma frase pelo teclado e mostre:
# Quantas veses aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

fra = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(fra.count('A')))
print('A frase  possui {} letras' .format(len(fra)))
print('A primeira letra A apareceu na posição {}'.format(fra.upper().find('A')+1))
print('A ultima letra A aparece na posição {}'.format(fra.rfind('A')+1))