import math
a=int(input("enter your a:"))
b=int(input("enter your b:"))
c=int(input("enter your c:"))
if a ==0:
    if b ==0:
        if c==0:
            print("l'ensemble des solutions est l'ensemble vide")
        else:
             print("l'ensemble des solutions est l'ensemble R") 
    else :
        x=c/b
        print("la solution est unique x = ",x)  
else :
    d=b*b-(4*a*c)
    if d<0  :
              print("l'ensemble des solutions est l'ensemble vide")
    else :
         if d ==0 :
                  print("la solution est unique x = ",(-b/2*a))  
         else :
              print("l'ensemble des solutions est x1=",(-b-math.sqrt(d))/(2*a), "et x2=",(-b+math.sqrt(d))/(2*a))

             
