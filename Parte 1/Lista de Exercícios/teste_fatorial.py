def fatorial(n):
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    return fat

def testa_fatorial():
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não unciona para 0")
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não unciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não unciona para 2")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não unciona para 5")
        
#n = int(input())
testa_fatorial()
