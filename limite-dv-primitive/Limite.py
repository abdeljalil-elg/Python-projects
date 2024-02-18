#abdeljalilelgadi
#how to calculate limit of function.



import sympy as sp

def ma_limite(fct, point):
    # Définit la variable symbolique
    x = sp.symbols('x')
    
    # Convertit la fonction entrée en une expression sympy
    expression = sp.sympify(fct)
    
    # Calcule la limite de la fonction en un point
    limite = sp.limit(expression, x, point)
    
    return limite

def main():
    fct = input("Entrez la fonction (par exemple, 'x**2 + 1/x') : ")
    point = input("Entrez le point pour lequel vous souhaitez calculer la limite (par exemple, 'oo' pour l'infini) : ")
    
    try:
        limite = ma_limite(fct, point)
        print("La limite de la fonction", fct, "en", point, "est :", limite)
    except Exception as e:
        print("Une erreur s'est produite lors du calcul de la limite :", e)

if __name__ == "__main__":
    main()
