largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
i = 1
j = 1
while i <= altura:
    while j <= largura:
        if (not (j > 1 and j < largura) ) or not (i > 1 and i < altura):
            print("#", end = "")
        else:
            print(" ", end = "")
        j = j + 1
    print()
    i = i + 1
    j = 1
