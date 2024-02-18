from sympy import symbols, Function, series, sympify

def developpement_limite():
    # Demander à l'utilisateur d'entrer la fonction
    expression = input("Entrez la fonction : ")
    x = symbols('x')
    
    try:
        # Convertir l'expression en une fonction SymPy
        f = sympify(expression)
        
        # Demander à l'utilisateur d'entrer le point autour duquel développer la fonction
        point = float(input("Entrez le point autour duquel vous souhaitez développer la fonction : "))
        
        # Demander à l'utilisateur d'entrer l'ordre du développement
        ordre = int(input("Entrez l'ordre du développement : "))
        
        # Calculer le développement limité de la fonction autour du point spécifié jusqu'à l'ordre spécifié
        expansion = series(f, x, point, ordre).removeO()
        
        print("Le développement limité de la fonction f(x) autour de x =", point, "jusqu'à l'ordre", ordre, "est :")
        print(expansion)
    except Exception as e:
        print("Une erreur s'est produite :", e)

# Appeler la fonction principale
developpement_limite()
