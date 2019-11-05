size=5
lista=[]
for i in range(size):
    lista.append(int(input("Elemento:")))
l=[]
for i in lista:
    if i not in l:
        l.append(i)
        count=0
        for j in lista:
            if j==i:
                count+=1
        if count>1:
            print("Elemento %s apareceu %d vezes."%(i,count))
        