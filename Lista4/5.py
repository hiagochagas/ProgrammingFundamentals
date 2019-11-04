size=20
lista=[]
lista_nova=[]
for a in range(size):
    lista.append(int(input("Entrada:")))
for a in lista[::-1]:
    lista_nova.append(a)
print("Lista nova:",lista_nova)