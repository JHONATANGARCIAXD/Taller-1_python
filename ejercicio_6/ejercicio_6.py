import math


# input

a=int(input("Digite el Valor de a: "))
b=int(input("Digite el Valor de b: "))
c=int(input("Digite el Valor de c: "))

# processing
x1=0
x2=0

if ((b**2)- 4*a*c)<0:
    print("Raices imaginarias o complejas")
else:
    x1=(-b + math.sqrt(b**2-(4*a*c)))/(2*a)
    x2=(-b -math. sqrt(b**2-(4*a*c)))/(2*a)
    print("El resultado de X1 es",x1)
    print("El resultado de X2 es",x2)
    print("Dos raices Reales Diferentes")
    if x1==x2:
        print("Dos Raices Reales iguales")


    







    
  
