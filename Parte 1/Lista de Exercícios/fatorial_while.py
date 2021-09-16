def fatorial(n):
    fatorial = n
    i = n    
    fatorial = 1
    while i > 1:
        fatorial = fatorial * i
        i = i - 1
    print("O fatorial de", n,"é:", fatorial)
n = 0
while n >= 0:
    n = int(input("Digite um número inteiro: "))
    if n >= 0:
        fatorial(n)
