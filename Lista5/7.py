def inverter_linha(matriz):
    res=[]
    for i in range(len(matriz)):
        linha=[]
        for j in range(len(matriz[i])):
            linha.append(matriz[i][len(matriz[i])-j-1])
        res.append(linha)
    return res
matriz=[[1,2,3],[4,5,6]]
print(inverter_linha(matriz))