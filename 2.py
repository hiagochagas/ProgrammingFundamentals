def multiplo_tres(n):
    if(n):
        return (n-1)*3
    else:
        multiplo_tres(n-1)
n=int(input())
if(n>0):
    print(multiplo_tres(n))