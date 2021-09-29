def Primo(n):
    d = 2
    EhPrimo = True
    if (n <= 1):
        EhPrimo = False

    while (EhPrimo) and (d <= n / 2):
        if (n % d  == 0):
            EhPrimo = False
        d = d + 1
        
    return EhPrimo

def n_primos(n):
    i = 0
    while n >= 2:
        if Primo(n):
            i = i + 1
        n = n - 1
    return i

n = int(input())
if n >= 2:
    print(n_primos(n))
