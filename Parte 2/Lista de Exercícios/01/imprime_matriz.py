def imprime_matriz(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])   
    for i in range(num_linhas):
        for j in range(num_colunas):
            if j < num_colunas - 1:
                print(matriz[i][j], end=" ")
            else:
                print(matriz[i][j])

    
        
