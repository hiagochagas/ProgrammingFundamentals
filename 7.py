def fatorial(x):
    fat=1
    for i in range(1,x+1):
        fat=fat*i
    return fat
def expressao(n):
    e=1
    for i in range (1,n+1):
        e=e+(1/fatorial(i))
    return e
n=int(input("N:"))
print("E =",expressao(n))
