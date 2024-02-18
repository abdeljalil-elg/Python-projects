import sympy as sp

def calculer_derivee(fonction):
    # Convertit la fonction en une expression sympy
    x = sp.symbols('x')
    expression = sp.sympify(fonction)
    
    # Calcule la dérivée de la fonction par rapport à x
    derivee = sp.diff(expression, x)
    
    return derivee

def main():
    fonction = input("Entrez la fonction pour calculer sa dérivée : ")
    
    try:
        derivee = calculer_derivee(fonction)
        print("La dérivée de la fonction", fonction, "est :", derivee)
    except Exception as e:
        print("Une erreur s'est produite lors du calcul de la dérivée :", e)

if __name__ == "__main__":
    main()
