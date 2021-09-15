n = int(input())
d = 2
EhPrimo = True
if (n <= 1):
    EhPrimo = False

while (EhPrimo) and (d <= n / 2):
    if (n % d  == 0):
        EhPrimo = False
    d = d + 1

if (EhPrimo):
    print("primo")
else:
    print("não primo")
