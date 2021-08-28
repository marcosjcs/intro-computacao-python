def soma(x, y):
    return x + y
def multiplica(x, y):
    m = 0
    if y == 1:
        return x
    while y >= 1:
        m = soma(m, x)
        y = y - 1
    return m
print(soma(10,20))
print(multiplica(10,20))
