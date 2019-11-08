def produto_listas(lista1,lista2):
    if (len(lista1))==0:
        return lista1
    else:
        lista1[0]*=lista2[0]
        return lista1[0:1] + produto_listas(lista1[1:],lista2[1:])
tipos=[]
preços=[]
quantidade_vendidos=[]
x=int(input("Quantos tipos de produtos você vende?"))
for i in range(x):
    print("Qual o nome do produto %d?"%(i+1))
    tipos.append(input())
    print("Qual o preço do produto '%s'?"%tipos[i])
    preços.append(float(input()))
    print("Quantos produtos do tipo '%s' você vendeu?"%tipos[i])
    quantidade_vendidos.append(int(input()))
vendas=produto_listas(preços,quantidade_vendidos)
for i in range(x):
    print("Você vendeu %d produtos do tipo '%s', totalizando R$ %.2f em vendas."%(quantidade_vendidos[i],tipos[i],vendas[i]))


#print(produto_listas(l1,l2))