#NIM game

def inicio(n, m):
    if n % (m + 1) == 0:
        print("Você começa!")
        return False
    else:
        print("Computador começa!")
        return True

def computador_escolhe_jogada(n, m):
    i = 1
    while i <= m:
        if (n - i) % (m + 1) == 0:
            return i        
        i = i + 1
    return m

def usuario_escolhe_jogada(n, m):
    j = 0
    while j <= 0: 
        j = int(input("Quantas peças você vai tirar? "))
        if j > m or j <= 0 or j > n:
            print("Oops! Jogada inválida! Tente de novo.")
            j = 0

    return j

def estado(jogador, n, nPecas):
    print(jogador,"tirou", n, "peça(s).")
    if (nPecas == 0):        
        print(jogador, "ganhou!")
        if jogador == "O computador":
            return True
        else:
            return False
    else:
        print("Agora resta(m) apena(s)", nPecas, "peça(s) no tabuleiro.")

def partida():
    voce = "Você"
    computador = "O computador"
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    nPecas = n
    j = 0
    c = 0
    
    vez = inicio(n, m)
    vencedor = False
    while nPecas > 0:        
        if vez:
            c = computador_escolhe_jogada(nPecas, m)
            nPecas = nPecas - c
            vencedor = estado(computador, c, nPecas)
            vez = False
        else:
            j = usuario_escolhe_jogada(nPecas, m)
            nPecas = nPecas - j        
            vencedor = estado(voce, j, nPecas)
            vez = True
    return vencedor

def campeoanato():
    nPartidas = 1
    placar = 0
    voce = 0
    while nPartidas <= 3:
        print("**** Rodada",nPartidas,"****")
        if partida():
            placar = placar + 1
        else:
            voce = voce + 1
        nPartidas = nPartidas + 1
        
    print("Placar: Você",voce, "X", placar,"Computador")
        
def main():
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    e = int(input())
    if e == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    else:
        if e == 2:
            print("Você escolheu um campeonato!")
            campeoanato()

main()
