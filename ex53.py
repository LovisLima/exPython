# Crie um programa que leia uma frase qualquer e diga se
# ela é um palidromo, desconsiderando os espaços


frase = str(input(" Digite a frase ou palavra: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1 ,-1, -1):
    inverso += junto[letra]
if inverso == junto:
    print ( 'É um palindromo')
else:
    print('Não é um palindromo')

print('voce digitou a frase {}'. format(frase))
