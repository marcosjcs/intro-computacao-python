largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
i = 1
j = 1
while i <= altura:
    while j <= largura:
        print("#", end = "")
        j = j + 1
    print()
    i = i + 1
    j = 1
