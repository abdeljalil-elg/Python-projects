#calculer la dérivée
#abdeljalilelgadi
import sympy as sp

def my_derivee(fct):
    # Convertit la fonction en une expression sympy
    x = sp.symbols('x')
    expression = sp.sympify(fct)
    
    # Calcule la dérivée de la fonction par rapport à x
    derivee = sp.diff(expression, x)
    
    return derivee

def main():
    fct = input("Entrez la fonction pour calculer sa dérivée : ")
    
    try:
        derivee = calculer_derivee(fct)
        print("La dérivée de la fonction", fct, "est :", derivee)
    except Exception as e:
        print("Une erreur s'est produite lors du calcul de la dérivée :", e)

if __name__ == "__main__":
    main()
