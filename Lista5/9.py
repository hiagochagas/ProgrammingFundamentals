def transposta(matriz):
    res=[]
    for j in range(len(matriz[0])):
        linha=[]
        for i in range(len(matriz)):
            linha.append(matriz[i][j])
        res.append(linha)
    return res
matriz=[[1,5],[7,3],[8,2]]
print(transposta(matriz))