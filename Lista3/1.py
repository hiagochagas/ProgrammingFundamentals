def mmc(x1,x2,x3):
    maximo=x1*x2*x3
    for a in range(2,maximo):
        if a%x1==0 and a%x2==0 and a%x3==0:
            return a
    return maximo
def lin_prod(x,y,z):
    paga=mmc(x,y,z)
    print("O pagamento deve ser feito depois de",paga,"dias.")
x=int(input("X:"))
y=int(input("Y:"))
z=int(input("Z:"))
lin_prod(x,y,z)