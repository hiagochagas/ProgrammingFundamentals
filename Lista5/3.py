m=[]
res=[]
linhas=int(input("Deseja quantas linhas na sua matriz?"))
colunas=int(input("Deseja quantas colunas na sua matriz?"))
for i in range(linhas):
    maior=menor=None
    l=[]
    for j in range(colunas):
        n=int(input("N:"))
        l.append(n)
        if(maior==None or n>maior):
            maior=n
        if(menor==None or n<menor):
            menor=n
    res.append([maior,menor])   
    m.append(l)
print("Maior e Menor")
print(res)