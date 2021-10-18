def fatorial(n):
    if n < 0:
        return 0
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    return fat

def testa_fatorial0():
    assert fatorial(0) == 1
    
def testa_fatorial1():
    assert fatorial(1) == 1

def testa_fatorial2():
    assert fatorial(2) == 2

def testa_fatorial3():
    assert fatorial(3) == 6

def testa_fatorial4():
    assert fatorial(4) == 24

def testa_fatorial_negativo():
    assert fatorial(-4) == 0
    
