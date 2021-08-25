par = 0
impar = 0
n = int(input())
while n > 0:
    numero = int(input())
    if (numero % 2) == 0:
        par = par + 1
    else:
        impar = impar + 1
    n = n - 1
print(par,"pares")
print(impar,"ímpares")
