def posicoes(lista, valor):
    resultado=[]
    for a in range(len(lista)):
        if lista[a]==valor:
            resultado.append(a)
    return resultado
lista=[]
qtd=int(input("Quantidade de elementos da lista:"))
for i in range(qtd):
    lista.append(int(input("Entrada:")))
menor=1000
for i in lista:
    if i<menor:
        menor=i
print("O menor número é:",menor)
print("O número",menor,"aparece nas seguintes posições:",posicoes(lista,menor))
    