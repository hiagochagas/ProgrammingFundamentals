def fatorial(x):
    if x>1:
        return x*fatorial(x-1)
    else:
        return 1
def soma_serie(qtd_termos,x):
    divisor=1
    a=-1
    S=0
    for i in range (2,qtd_termos+2):
        S+=a*(x**i)/fatorial(divisor)
        a*=-1
        divisor+=1
        if divisor==5:
            divisor=1
    return S
qtd_termos=int(input("Quantidade de termos:")) # recomendo testar com 1 e 1
x=int(input("Valor de X:"))
print("S =",soma_serie(qtd_termos,x))
