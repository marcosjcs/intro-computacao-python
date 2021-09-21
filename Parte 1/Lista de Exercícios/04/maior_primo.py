def ehPrimo(n):
    d = 2
    EhPrimo = True
    if (n <= 1):
        EhPrimo = False

    while (EhPrimo) and (d <= n / 2):
        if (n % d  == 0):
            EhPrimo = False
        d = d + 1
        
    return EhPrimo

def maior_primo(k):
    while k >= 2:
        if ehPrimo(k):
            return k
        k = k - 1
    return
