import math
def menor_distancia(x,y,lista_pontos):
    menor_distancia=1000
    ponto=[]
    for i in range(len(lista_pontos)):
        if i%2!=0:
            continue
        else:
            if x>lista_pontos[i]:
                distancia=math.sqrt(((x-lista_pontos[i])**2)+((y-lista_pontos[i+1])**2))
            else:
                distancia=math.sqrt(((lista_pontos[i]-x)**2)+((lista_pontos[i+1]-y)**2))
        if distancia<menor_distancia:
            menor_distancia=distancia
    return menor_distancia
lista_pontos=[]
qtd=int(input("Quantidade de pontos:"))
for i in range(qtd):
    print("X%d:"%(i+1))
    lista_pontos.append(int(input()))
    print("Y%d:"%(i+1))
    lista_pontos.append(int(input()))
x=int(input("Qual o ponto X?:"))
y=int(input("Qual o ponto Y?:"))
print(menor_distancia(x,y,lista_pontos))

#continuar mais tarde rsrs
#falta colocar a função vizinhos_mais_proximos