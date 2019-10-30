def aluno_media(nota1, nota2):
    media=((nota1*2)+(nota2*3))/5
    return media
def situacao_aluno(media):
    if media>=7:
        return "Aprovado!"
    elif media<3:
        return "Reprovado!"
    else:
        return "Recuperação!"
def situacao_final(media, nota_final):
    media_final=(media+nota_final)/2
    if media_final>=5:
        return "Aprovado na Recuperação!"
    else:
        return "Reprovado na Recuperação!"
qtd=int(input("Quantidade de alunos:"))
for i in range(qtd):
    nota1=float(input("Nota 1 do aluno %d:"%(i+1)))
    nota2=float(input("Nota 2 do aluno %d:"%(i+1)))
    media=aluno_media(nota1,nota2)
    print(situacao_aluno(media))
    if media<7:
        notafinal=float(input("Nota final do aluno %d:"%(i+1)))
        print(situacao_final(media,notafinal))