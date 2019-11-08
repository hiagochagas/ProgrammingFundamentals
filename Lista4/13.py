def soma_quase_todos(lista,x,i):
  if len(lista)<1:
    return lista
  else:
    #print(lista)
    if i>=0:
      if(i!=0):
        lista[0]+=x
    else:
      lista[0]+=x
    #print(lista,x)
    return lista[0:1] + soma_quase_todos(lista[1:],x,i-1)
l=[]
tam=int(input("Tamanho da lista:"))
for a in range(tam):
  l.append(int(input("Elemento da lista:")))
x=int(input("Quanto deseja adicionar em cada elemento?"))
i=int(input("Qual posição da lista você deseja que não seja alterada? Ex.:0,1"))
print("Lista resultado:",soma_quase_todos(l,x,i))