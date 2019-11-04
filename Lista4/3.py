qtd=10
nomes=[]
quantidade_anos_trabalhados=[]
salarios=[]
for a in range(qtd):
    print("Nome do empregado %d:"%(a+1))
    nomes.append(input())
    print("Salario de %s:"%nomes[a])
    salarios.append(float(input()))
    print("Há quantos anos o %s é nosso colaborador?"%nomes[a])
    quantidade_anos_trabalhados.append(int(input()))
media_salarial=sum(salarios)/qtd
for a in range(qtd):
    if salarios[a]<media_salarial and quantidade_anos_trabalhados[a]>=5:
        salarios[a]=salarios[a]*1.35
    elif salarios[a]<media_salarial or quantidade_anos_trabalhados[a]>=5:
        salarios[a]=salarios[a]*1.10
    print("Salario de %s: R$ %.2f:"%(nomes[a],salarios[a]))