def fatorial_duplo(n):
    if n>0:
        return n*fatorial_duplo(n-2)
    else:
        return 1
n=int(input("Fatorial duplo:"))
print(fatorial_duplo(n))