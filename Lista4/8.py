def media_lista(lista):
    soma=0
    qtd=0
    for a in lista:
        qtd+=1
        soma+=a
    return soma/qtd
turma1=[]
turma2=[]
qtd_t1=int(input("Quantidade de alunos na turma 1:"))
for a in range(qtd_t1):
    turma1.append(float(input("Nota do aluno:")))
qtd_t2=int(input("Quantidade de alunos na turma 2:"))
for a in range(qtd_t2):
    turma2.append(float(input("Nota do aluno:")))
media_t1=media_lista(turma1)
media_t2=media_lista(turma2)
acima=abaixo=namedia=0
for a in turma1:
    if a>media_t1:
        acima+=1
    elif a==media_t1:
        namedia+=1
    else:
        abaixo+=1
print("%d aluno(s) da turma 1 na média, %d aluno(s) abaixo da média e %d aluno(s) acima da média"%(namedia,abaixo,acima))
acima=abaixo=namedia=0
for a in turma2:
    if a>media_t2:
        acima+=1
    elif a==media_t2:
        namedia+=1
    else:
        abaixo+=1
print("%d aluno(s) da turma 2 na média, %d aluno(s) abaixo da média e %d aluno(s) acima da média"%(namedia,abaixo,acima))