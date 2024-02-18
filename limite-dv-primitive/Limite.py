import sympy as sp

def calculer_limite(fonction, point):
    # Définit la variable symbolique
    x = sp.symbols('x')
    
    # Convertit la fonction entrée en une expression sympy
    expression = sp.sympify(fonction)
    
    # Calcule la limite de la fonction en un point
    limite = sp.limit(expression, x, point)
    
    return limite

def main():
    fonction = input("Entrez la fonction (par exemple, 'x**2 + 1/x') : ")
    point = input("Entrez le point pour lequel vous souhaitez calculer la limite (par exemple, 'oo' pour l'infini) : ")
    
    try:
        limite = calculer_limite(fonction, point)
        print("La limite de la fonction", fonction, "en", point, "est :", limite)
    except Exception as e:
        print("Une erreur s'est produite lors du calcul de la limite :", e)

if __name__ == "__main__":
    main()
