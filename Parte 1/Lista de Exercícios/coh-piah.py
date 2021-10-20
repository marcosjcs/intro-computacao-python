import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    soma = 0
    similaridade = 0
    while i < 6:
        soma = soma + abs(as_a[i] - as_b[i])        
        i = i + 1
    similaridade = soma / 6
    return similaridade

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_sentencas = []
    lista_frases = []
    lista_palavras = []    
    lista_sentencas = separa_sentencas(texto)
    
    for sentenca in lista_sentencas:
        lista_frases = lista_frases + separa_frases(sentenca)
    for frase in lista_frases:
        lista_palavras = lista_palavras + separa_palavras(frase)

    wal = tam_medio_palavra(lista_palavras)
    ttr = type_token(lista_palavras)
    hlr = hapax_legomana(lista_palavras)
    sal = tam_medio_sentenca(lista_sentencas)
    sac = complexidade_sentenca(lista_sentencas)
    pal = tam_medio_frase(lista_frases)
    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    grau_similaridade = []
    menor = 0
    i = 0
    for texto in textos:
        grau_similaridade.append(compara_assinatura(ass_cp, calcula_assinatura(texto)))

    while i < len(grau_similaridade) - 1:
        if grau_similaridade[menor] > grau_similaridade[i+1]:
            menor = i + 1
        i = i + 1
    return menor + 1

def total_palavras(lista_palavras):
    return len(lista_palavras)

def total_sentencas(lista_sentencas):
    return len(lista_sentencas)

def total_frases(lista_frases):
    return len(lista_frases)

def tam_medio_palavra(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e retorna o tamanho medio das palavras'''
    soma_tamanho_palavras = 0    
    for x in lista_palavras:
        soma_tamanho_palavras = soma_tamanho_palavras + len(x)    
    return soma_tamanho_palavras / total_palavras(lista_palavras)
    
def type_token(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e retorna a divisao do numero de palavras diferentes dividido pelo total de palavras'''
    return n_palavras_diferentes(lista_palavras) / total_palavras(lista_palavras)

def hapax_legomana(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e retorna a divisao do numero de palavras que aparecem uma unica vez dividido pelo total de palavras'''
    return n_palavras_unicas(lista_palavras) / total_palavras(lista_palavras)

def tam_medio_sentenca(lista_sentencas):
    '''Essa funcao recebe uma lista de sentencas e retorna a divisao da soma dos numeros de caracteres em todas as sentencas dividido pelo total de setencas'''
    soma_tamanho_sentencas = 0
    for x in lista_sentencas:
        soma_tamanho_sentencas = soma_tamanho_sentencas + len(x)
    return soma_tamanho_sentencas / total_sentencas(lista_sentencas)

def complexidade_sentenca(lista_sentencas):
    '''Essa funcao recebe uma lista de setencas e retorna a divisao do numero total de frases dividido pelo total de setencas'''
    total_frases = 0
    for sentenca in lista_sentencas:
        total_frases = total_frases + len(separa_frases(sentenca))
    return total_frases / total_sentencas(lista_sentencas)

def tam_medio_frase(lista_frases):
    '''Essa funcao recebe uma lista de frases e retorna a divisao da soma dos numeros de caracteres em todas as frases dividido pelo total de frases'''
    soma_tamanho_frases = 0
    for x in lista_frases:
        soma_tamanho_frases = soma_tamanho_frases + len(x)
    return soma_tamanho_frases / total_frases(lista_frases)

def main():
    
    ass_cp = le_assinatura()
    
    textos = le_textos()

    print("O autor do texto", avalia_textos(textos, ass_cp),"está infectado com COH-PIAH")
    
main()
