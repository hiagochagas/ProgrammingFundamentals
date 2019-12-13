def soma_diagonal_secundaria(matriz):
    soma=0
    for i in range(len(matriz)):
        soma+=matriz[i][len(matriz)-1-i]
    return soma
def soma_diagonal_principal(matriz):
    soma=0
    for i in range(len(matriz)):
        soma+=matriz[i][i]
    return soma
def soma_linha(matriz,linha):
    soma=0
    for i in range(len(matriz[linha])):
        soma+=matriz[linha][i]
    return soma
def soma_coluna(matriz,coluna):
    soma=0
    for i in range(len(matriz)):
        soma+=matriz[i][coluna]
    return soma
def verifica_quadrado(matriz):
    l=[]
    l.append(soma_diagonal_principal(matriz))
    l.append(soma_diagonal_secundaria(matriz))
    for i in range(len(matriz)):
        l.append(soma_linha(matriz,i))
    for j in range(len(matriz[0])):
        l.append(soma_coluna(matriz,j))
    for i in l:
        if i!=l[0]:
            return False
    return True
matriz=[[2,7,6],[9,5,1],[4,3,8]]
print(verifica_quadrado(matriz))
