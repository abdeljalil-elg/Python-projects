import math
try:
    x= int(input("entrez votre nombre:"))
    y= str(input("entrer votre opérateur:"))
    z= int(input("entrez votre nombre:"))
except ValueError: 
    print("invalid literal")
match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)    
    case "*":
        print(x*z)  
    case "/":
        try:
            print(x/z) 
        except ZeroDivisionError:
            print ("ops c'est impossible")    
    case "%" :
        print(x%z)
    case _:
        print("Je ne connais pas ce opérateur.")     
        
