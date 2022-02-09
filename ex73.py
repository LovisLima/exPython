#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 'Brasileirao.
# na ordem de colocação. Depois mostre:
# Os cinco primeiros colocados
# Ultimos quatro colocados
# Times em ordem alfabetica
# Em que posiçao está o time da chapecoense

times= ('Atletico - MG','Flamengo', 'Palmeiras', 'Fortaleza','Corintians', 'RB-Bragantimo', 'Fluminense',
'America-MG', 'Atletico-GO','Santos','Ceará','Internacional','Sao Paulo','Atletico-PR','Cuiabá','Juventude',
'Grêmio','Bahia','Sport','Chapecoense')

print(sorted(times))
print(times[:5])
print(times[-4:])
print(f'O chapecoense está na {times.index ("Chapecoense")+1}º posição')