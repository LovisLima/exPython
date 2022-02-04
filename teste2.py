
n = int(input("Que termo deseja encontrar ?: "))

u=1
p=1

if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = u + p
        p = u
        u = termo
        count += 1
    print(termo)


m = int(input("Digite um valor: "))
m = termo

if m == termo:
    print("é fibonacci")

else:
    m != termo
    print("nao eh fibonacci")


