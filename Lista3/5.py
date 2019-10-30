def soma_naturais(n):
    soma=0
    if (n>0):
        return n+soma_naturais(n-1)
    else:
        return n
n=int(input("Quantidade de nums:"))
print(soma_naturais(n))