n = 1
lista = []
while n > 0:
    n = int(input("Digite um número: "))
    if n != 0:
        lista.append(n)

for x in range(len(lista),0,-1):
    print(lista[x-1])

