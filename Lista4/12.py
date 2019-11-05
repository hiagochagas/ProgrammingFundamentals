size=3
alturas=[]
for i in range(size):
    alturas.append(float(input("Altura:")))
media_alturas=sum(alturas)/len(alturas)
mais_repetida=0
count=0
for i in alturas:
    aux=0
    for j in alturas:
        if j==i:
            aux+=1
    if aux>count:
        count=aux
        mais_repetida=i
print("Mais repetida:",mais_repetida)
print("Media das alturas:",media_alturas)