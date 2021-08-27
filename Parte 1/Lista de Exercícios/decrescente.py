decrescente = True
anterior = int(input("Digite o primeiro número da seq:"))

valor =  1
while valor != 0 and decrescente:
    valor = int(input("Digite o próximo número da seq:"))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print("Decrescente")
else:
    print("Não decrescente")
