def ordena_decrescente(lista):
    maior=0
    lista_decrescente=[]
    i=0
    size=len(lista)
    for i in range(size):
        maior=0
        for j in range(len(lista)):
            if lista[j]>=maior:
                maior=lista[j]
        lista_decrescente.append(maior)
        del lista[lista.index(maior)]
    return lista_decrescente
t1=[]
t2=[]
t3=[]
x=int(input("Quantos alunos há na turma 1?"))
for j in range(x):
    print("Nota do aluno %d:"%(j+1))
    t1.append(float(input()))
x=int(input("Quantos alunos há na turma 2?"))
for j in range(x):
    print("Nota do aluno %d:"%(j+1))
    t2.append(float(input()))
x=int(input("Quantos alunos há na turma 3?"))
for j in range(x):
    print("Nota do aluno %d:"%(j+1))
    t3.append(float(input()))
print("Notas da turma 1:",ordena_decrescente(t1))
print("Notas da turma 2:",ordena_decrescente(t2))
print("Notas da turma 3:",ordena_decrescente(t3))
