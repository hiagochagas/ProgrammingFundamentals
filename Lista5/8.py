def troca_linhas(matriz,indice_lin1,indice_lin2):
    res=[]
    for i in range(len(matriz)):
        if i == indice_lin1:
            res.append(matriz[indice_lin2])
        elif i == indice_lin2:
            res.append(matriz[indice_lin1])
        else:
            res.append(matriz[i])
    return res
matriz=[[1,2],[3,4],[5,6]]
print(troca_linhas(matriz,0,2))