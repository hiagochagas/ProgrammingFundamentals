#Construa uma função ordena_por_frequencia(lista) que recebe uma lista como parâmetro
#e retorna a lista ordenada pela frequencia dos seus elementos. Por exemplo,
#ordena_por_frequencia([2, 5, 2, 8, 5, 6, 8, 8]) deve retornar a lista [8, 8, 8, 2, 2, 5, 5, 6].
#A ordem dos elementos com mesma frequência não importa.
def ordena_por_frequencia(lista):
    result=[]
    contagem=[]
    elementos=[]
    for i in lista:
        if i not in elementos:
            elementos.append(i)
            contagem.append(lista.count(i))
    for i in range(len(elementos)):
        count=max(contagem)
        for j in range(count):
            result.append(elementos[contagem.index(count)])
        del elementos[contagem.index(count)]
        del contagem[contagem.index(count)]
        print("a",result)
    return result
print(ordena_por_frequencia([1,3,2,2,3,3,5]))
    