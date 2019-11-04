def primo(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
size=10
lista=[]
primos=[]
for i in range(size):
    lista.append(int(input("Entrada:")))
    if primo(lista[i])==True:
        primos.append(i)
print("Posições dos números primos:",primos)