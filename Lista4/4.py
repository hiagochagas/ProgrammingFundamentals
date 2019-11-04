def intersecao(lista1,lista2):
    lista=[]
    for a in lista1:
        if a in lista2:
            lista.append(a)
    return lista
empregados=[]
gerentes=[]
qtd_empregados=int(input("Quantos empregados há na empresa?"))
for i in range (qtd_empregados):
    print("Digite o nome do empregado %d:"%(i+1))
    empregados.append(input())
qtd_gerentes=int(input("Quantos gerentes há na empresa?"))
for i in range (qtd_gerentes):
    gerentes.append(input())
print("Esses empregados são gerentes:",intersecao(empregados,gerentes))