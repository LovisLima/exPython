def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [7,2,5,2,5,4]
dobra(valores)
print(valores)