n = int(input())
adjacente = False
atual = -1
anterior = -1
while n > 0:
    atual = n % 10
    if atual == anterior:
        adjacente = True
    anterior = atual
    n = n // 10
if adjacente:
    print("sim")
else:
    print("não")

