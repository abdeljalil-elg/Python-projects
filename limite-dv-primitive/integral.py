import sympy as sp

def main():
    # Demander à l'utilisateur d'entrer la fonction
    expression = input("Entrez la fonction à intégrer en utilisant x comme variable : ")
    
    # Convertir l'expression en une fonction sympy
    x = sp.Symbol('x')
    f = sp.sympify(expression)
    
    # Demander à l'utilisateur d'entrer les bornes de l'intégrale
    a = float(input("Entrez la borne inférieure de l'intégrale : "))
    b = float(input("Entrez la borne supérieure de l'intégrale : "))
    
    # Calculer l'intégrale en utilisant la méthode des trapèzes
    integral = sp.integrate(f, (x, a, b))
    
    print("L'intégrale de", expression, "de", a, "à", b, "est :", integral)

if __name__ == "__main__":
    main()
