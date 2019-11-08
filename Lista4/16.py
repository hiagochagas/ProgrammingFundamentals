def palindromo(lista):
  if len(lista)<=1:
    return True
  else:
    if(lista[0]==lista[(len(lista)-1)]):
      #print(lista) 
      return True and palindromo(lista[1:len(lista)-1])
    else:
      return False
lista=[]
x=int(input("Tamanho da lista:"))
for i in range(x):
  lista.append(int(input("Elemento:")))
resultado=palindromo(lista):
if resultado:
  print("A lista é um palíndromo.")
else:
  print("A lista não é um palíndromo.")
