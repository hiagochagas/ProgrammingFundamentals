def soma_diagonal_secundaria(matriz):
    soma=0
    for i in range(len(matriz)):
        soma+=matriz[i][len(matriz)-1-i]
    return soma

matriz=[[0,1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5,6]]
print(soma_diagonal(matriz))
