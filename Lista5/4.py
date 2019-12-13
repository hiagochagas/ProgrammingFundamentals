distancias_fortaleza=[[3400,"Curitiba"],[600,"Natal"],[3000, "São Paulo"],[2500,"Rio de Janeiro"]]
distancias_natal=[[3300,"Curitiba"],[600,"Fortaleza"],[2900, "São Paulo"],[2600,"Rio de Janeiro"] ]
distancias_saopaulo=[[416,"Curitiba"],[2900,"Natal"],[3000, "Fortaleza"],[430,"Rio de Janeiro"] ]
distancias_rio=[[840,"Curitiba"],[2600,"Natal"],[430, "São Paulo"],[2500,"Fortaleza"] ]
distancias_curitiba=[[3400,"Fortaleza"],[3300,"Natal"],[416, "São Paulo"],[840,"Rio de Janeiro"] ]
def maior_menor(cidade,lista):
    maior=menor=lista[0][0]
    maior_cidade=menor_cidade=lista[0][1]
    for i in range(len(lista)):
        if lista[i][0]>maior:
            maior=lista[i][0]
            maior_cidade=lista[i][1]
        if lista[i][0]<menor:
            menor=lista[i][0]
            menor_cidade=lista[i][1]
    print("A maior distância de %s às outras cidades é de %d Km e é na cidade de %s. Já a menor é distância é de %d Km até %s."%(cidade,maior,maior_cidade,menor,menor_cidade))
print("Deseja saber qual itinerário é mais longo e próximo?\n1-Fortaleza\n2-Natal\n3-São paulo\n4-Rio de Janeiro\n5-Curitiba")
x=int(input())
if x==1:
    maior_menor("Fortaleza",distancias_fortaleza)
if x==2:
    maior_menor("Natal",distancias_natal)
if x==3:
    maior_menor("São Paulo",distancias_saopaulo)
if x==4:
    maior_menor("Rio de Janeiro",distancias_rio)
if x==5:
    maior_menor("Curitiba",distancias_curitiba)