m=[]
soma=0
linhas=int(input("Deseja quantas linhas na sua matriz?"))
colunas=int(input("Deseja quantas colunas na sua matriz?"))
for i in range(linhas):
    l=[]
    for j in range(colunas):
        n=int(input("N:"))
        l.append(n)
        if(n%2!=0):
            soma+=n
    m.append(l)
print(soma)
