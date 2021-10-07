def remove_repetidos(lista):
    x = len(lista) - 1    
    while x > 0:
        if lista[x] in lista[0:x]:            
            del lista[x]
        x = x - 1
    return sorted(lista)

