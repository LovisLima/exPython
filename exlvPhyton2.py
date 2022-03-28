from operator import add

def soma(x,y):
    return x + y

def sub (x,y):
    return x - y

def mul(x,y):
    return x * y


# teste soma
assert soma(5,5) == add(5,5)
#teste sub
assert sub(5,5) == 0, 'Erro no resultado de sub:{}'.format(sub(5,5))
#teste mul
assert mul(3,2) == 6
