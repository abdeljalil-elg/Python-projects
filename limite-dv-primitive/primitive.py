import sympy as sp

def calculer_primitive(fonction):
    # Convertit la fonction en une expression sympy
    x = sp.symbols('x')
    expression = sp.sympify(fonction)
    
    # Calcule la primitive de la fonction par rapport à x
    primitive = sp.integrate(expression, x)
    
    return primitive

def main():
    fonction = input("Entrez la fonction pour calculer sa primitive : ")
    
    try:
        primitive = calculer_primitive(fonction)
        print("La primitive de la fonction", fonction, "est :", primitive)
    except Exception as e:
        print("Une erreur s'est produite lors du calcul de la primitive :", e)

if __name__ == "__main__":
    main()
