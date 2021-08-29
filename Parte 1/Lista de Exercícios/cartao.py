meuCartao = int(input("Digite o número do cartão: "))

cartaoLido = 1
encontrei = False

while cartaoLido != 0 and not encontrei:
    cartaoLido = int(input("Digite o número do próximo cartão: "))
    if cartaoLido == meuCartao:
        encontrei = True

if encontrei:
    print("Encontrei")
else:
    print("Não encontrei")
