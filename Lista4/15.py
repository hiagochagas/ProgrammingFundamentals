def inverte_lista(lista):
    if len(lista)>1:
        aux=lista[0]
        lista[0]=lista[len(lista)-1]
        lista[len(lista)-1]=aux
        #print(lista)
        return lista[0:1] + inverte_lista(lista[1:len(lista)-1]) + lista[len(lista)-1:len(lista)]
    return lista    
l=[]
x=int(input("Digite o tamanho da lista:"))
for i in range(x):
    l.append(int(input("Entrada:")))
print(inverte_lista(l))