lista=[]
size=int(input("Tamanho da lista:"))
for i in range(size):
    lista.append(int(input("Entrada:")))
numero=int(input("Número a ser removido da lista:"))
i=0
while i<=size+1:
    if lista[i]==numero:
        lista.remove(numero)
    else:
        i+=1
    size-=1   
print("Lista nova:",lista)
#não funcionou direitinho