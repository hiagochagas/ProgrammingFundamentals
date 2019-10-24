def mdc(x1,x2,x3):
    maximo=max(x1,x2,x3)
    while maximo>0:
        if x1%maximo==0 and x2%maximo==0 and x3%maximo==0:
            return maximo
        maximo-=1
def grupos(x,y,z):
    tam=mdc(x,y,z)
    if tam>1:
        print((x+y+z)//tam,"barras de",tam,"centímetros.")
    else:
        print("As barras não puderam ser divididas")
x=int(input("X:"))
y=int(input("Y:"))
z=int(input("Z:"))
grupos(x,y,z)