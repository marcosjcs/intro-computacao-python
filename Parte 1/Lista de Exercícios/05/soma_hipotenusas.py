def soma_hipotenusas(n):
    soma = 0
    while n >= 1:
        if é_hipotenusa(n):
            soma =  soma + n
        n = n - 1
    return soma

def é_hipotenusa(n):
    i = 1
    j = 1
    while i <= n:
        while j <= n:
            if (n ** 2) == (i ** 2) + (j ** 2):
                return True
            j = j + 1
        j = 1
        i = i + 1
    return False
n = int(input()) 
print(soma_hipotenusas(n))
