m=[]
linhas=3
colunas=3
maior=None
for i in range(linhas):
    l=[]
    for j in range(colunas):
        n=int(input("N:"))
        l.append(n)
        if  maior==None or n>maior:
            maior=n
    m.append(l)
for i in range(linhas):
    for j in range(colunas):
        m[i][j]*=maior
print(m)