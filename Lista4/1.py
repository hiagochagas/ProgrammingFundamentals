size=5
modelos = []
preços = []
consumo = []
for i in range (size):
    print("Modelo %d:"%i+1)
    modelos.append(input())
    print("Preço do modelo %s:"%modelos[i])
    preços.append(float(input()))
    print("Consumo do modelo %s:"%modelos[i]) # quanto maior, melhor
    consumo.append(float(input()))
media_preços=sum(preços)/len(preços)
print("Média de Preços: R$ %.2f"%media_preços)
mais_economico=modelos[consumo.index(max(consumo))]
print("O modelo mais econômico é:",mais_economico)
for a in range(size):
    if preços[a]>media_preços:    
        litros=1000/consumo[a]
        print("O modelo %s precisa de %.2f litros para percorrer 1000Km"%(modelos[a],litros))