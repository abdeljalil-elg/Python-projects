# Solveur de Sudoku
# ABDELJALIL ELG

from tkinter import Tk,Canvas

# GUI

fenetre = Tk()
fenetre.title("Solveur de Sudoku - NSI")
fenetre.resizable(False,False)

interface = Canvas(fenetre,width=400,height=500,bg="white")
interface.pack()
interface.create_text(5,400,anchor="nw",text="Pour ajouter un chiffre, survolez la case correspondante et appuyez sur\nle pavé numérique.",tags="i")
interface.create_text(5,435,anchor="nw",text="Pour supprimer un chiffre, survolez la case et appuyez sur 'Effacer'.",tags="i")
interface.create_text(5,455,anchor="nw",text="Pour résoudre la grille, appuyez sur 'Entrer'.",tags="i")
interface.create_text(5,480,anchor="nw",text="Pour tout effacer, appuyez sur 'Suppr'.",tags="i")

interface.create_rectangle(12,7,15,379,fill="black")
interface.create_rectangle(381,7,384,379,fill="black")
interface.create_rectangle(12,7,384,10,fill="black")
interface.create_rectangle(12,376,384,379,fill="black")
cases = [[0]*9 for n in range(9)]
textCase = [[False]*9 for n in range(9)]
ic = 0
ie = 0
for i in range(15,369,40):
    jc = 0
    je = 0
    for j in range(10,364,40):
        cases[jc][ic] = interface.create_rectangle(i+ie,j+je,i+ie+40,j+je+40,fill="white",activefill="#e0e0e0")
        jc += 1
        if jc in [3,6]:
            interface.create_rectangle(12,j+43+je,384,j+40+je,fill="black")
            je += 3
    ic += 1
    if ic in [3,6]:
        interface.create_rectangle(i+43+ie,7,i+ie+40,379,fill="black")
        ie += 3

def event(touche):
    global grille,textCase,cases
    toucheK = touche.keysym
    if toucheK in "123456789":
        eff = False
        if interface.type(interface.find_closest(touche.x,touche.y)[0]) == "text" and interface.itemcget(interface.find_closest(touche.x,touche.y)[0],"tags") != "i current":
            interface.delete(interface.find_closest(touche.x,touche.y)[0])
            eff = True
        for i in range(9):
            for j in range(9):
                if interface.find_closest(touche.x,touche.y)[0] == cases[i][j]:
                    if not eff and not grille[i][j]:
                        grille[i][j] = int(toucheK)
                    if eff:
                        grille[i][j] = int(toucheK)
                        textCase[i][j] = False
                    break
            if interface.find_closest(touche.x,touche.y)[0] == cases[i][j]:
                break
        affG(i,j,toucheK)
    if toucheK == "Return":
        chercher()
    if toucheK == "Delete":
        nouv()
    if toucheK == "BackSpace":
        if interface.type(interface.find_closest(touche.x,touche.y)[0]) == "text" and interface.itemcget(interface.find_closest(touche.x,touche.y)[0],"tags") != "i current":
            interface.delete(interface.find_closest(touche.x,touche.y)[0])
            for i in range(9):
                for j in range(9):
                    if interface.find_closest(touche.x,touche.y)[0] == cases[i][j]:
                        grille[i][j] = 0
                        textCase[i][j] = False
                        break
                if interface.find_closest(touche.x,touche.y)[0] == cases[i][j]:
                    break

def affG(x=-1,y=-1,nb=-1):
    global textCase,cases
    if (x,y) == (-1,-1):
        for x in range(9):
            for y in range(9):
                if not textCase[x][y]:
                    interface.create_text((interface.coords(cases[x][y])[0]+interface.coords(cases[x][y])[2])//2,(interface.coords(cases[x][y])[1]+interface.coords(cases[x][y])[3])//2,anchor="center",text=str(grille[x][y]),font=("Helvetica","16","bold"),fill="#0f0fa0",tags="case")
    else:
        if not textCase[x][y]:
            textCase[x][y] = True
            interface.create_text((interface.coords(cases[x][y])[0]+interface.coords(cases[x][y])[2])//2,(interface.coords(cases[x][y])[1]+interface.coords(cases[x][y])[3])//2,anchor="center",text=nb,font=("Helvetica","16","bold"),tags="case")
    
fenetre.bind("<Key>",event)

# Moteur de resolution

def nouv():
    global grille,grilleFinie,textCase
    grille = [[0]*9 for n in range(9)]
    grilleFinie = [[False]*9 for n in range(9)]
    textCase = [[False]*9 for n in range(9)]
    interface.delete("case")

def solutions(l,c,ites):
    global grille,grilleFinie
    verifier()
    
    lc = l in [0,1,2] and [0,1,2] or l in [3,4,5] and [3,4,5] or l in [6,7,8] and [6,7,8]
    cc = c in [0,1,2] and [0,1,2] or c in [3,4,5] and [3,4,5] or c in [6,7,8] and [6,7,8]
    
    # Methode de recherche : Inclusion
    
    if not grilleFinie[l][c]:
        if not ites:
            grille[l][c] = [1,2,3,4,5,6,7,8,9]
        for k in range(9):
            if grilleFinie[l][k] and grille[l][k] in grille[l][c] and k != c:
                grille[l][c].remove(grille[l][k])
            if grilleFinie[k][c] and grille[k][c] in grille[l][c] and k != l:
                grille[l][c].remove(grille[k][c])
        for i in lc:
            for j in cc:
                if grilleFinie[i][j] and grille[i][j] in grille[l][c] and (i,j) != (l,c):
                    grille[l][c].remove(grille[i][j])
        verifier(l,c)
        
    # Methode de recherche : Exclusion (ap 1 iteration)
    
    if not grilleFinie[l][c] and ites:
        for nb in grille[l][c]:
            compteur = [0,0,0]
            for k in range(9):
                if not grilleFinie[l][k] and k != c:
                    for n in grille[l][k]:
                        compteur[0] += int(n == nb)
                if not grilleFinie[k][c] and k != l:
                    for n in grille[k][c]:
                        compteur[1] += int(n == nb)
            for i in lc:
                for j in cc:
                    if not grilleFinie[i][j] and (i,j) != (l,c):
                        for n in grille[i][j]:
                            compteur[2] += int(n == nb)
            if compteur[0] == 0 or compteur[1] == 0 or compteur[2] == 0:
                grilleFinie[l][c] = True
                grille[l][c] = nb   
                for k in range(9):
                    if not grilleFinie[l][k] and grille[l][c] in grille[l][k] and k != c:
                        grille[l][k].remove(grille[l][c])
                    if not grilleFinie[k][c] and grille[l][c] in grille[k][c] and k != l:
                        grille[k][c].remove(grille[l][c])
                for i in lc:
                    for j in cc:
                        if not grilleFinie[i][j] and grille[l][c] in grille[i][j] and (i,j) != (l,c):
                            grille[i][j].remove(grille[l][c])
                break
                
    # Methode de recherche : Paires exclusives
    
    if not grilleFinie[l][c] and ites and len(grille[l][c]) == 2:
        existe = [False,False,False]
        for k in range(9):
            if not grilleFinie[l][k] and grille[l][k] == grille[l][c] and k != c:
                existe[0] = True
            if not grilleFinie[k][c] and grille[k][c] == grille[l][c] and k != l:
                existe[1] = True
        for i in lc:
            for j in cc:
                if not grilleFinie[i][j] and grille[i][j] == grille[l][c] and (i,j) != (l,c):
                    existe[2] = True
        if existe[0]:
            for k in range(9):
                if not grilleFinie[l][k] and grille[l][k] != grille[l][c]:
                    for n in grille[l][k]:
                        if n in grille[l][c]:
                            grille[l][k].remove(n)
        if existe[1]:
            for k in range(9):
                if not grilleFinie[k][c] and grille[k][c] != grille[l][c]:
                    for n in grille[k][c]:
                        if n in grille[l][c]:
                            grille[k][c].remove(n)
        if existe[2]:
            for i in lc:
                for j in cc:
                    if not grilleFinie[i][j] and grille[i][j] != grille[l][c]:
                        for n in grille[i][j]:
                            if n in grille[l][c]:
                                grille[i][j].remove(n)
            
    # Methode de recherche : Triplets exculsifs (hors triplet induit)
            
    if not grilleFinie[l][c] and ites and len(grille[l][c]) == 3:
        existe = [[],[],[]]
        decompo = [[grille[l][c][0],grille[l][c][1]],[grille[l][c][1],grille[l][c][2]],[grille[l][c][0],grille[l][c][2]]]
        for k in range(9):
            if not grilleFinie[l][k] and k != c and (grille[l][k] == grille[l][c] or grille[l][k] in decompo):
                existe[0].append(grille[l][k])
            if not grilleFinie[k][c] and k != l and (grille[k][c] == grille[l][c] or grille[k][c] in decompo):
                existe[1].append(grille[k][c])
        for i in lc:
            for j in cc:
                if not grilleFinie[i][j] and (i,j) != (l,c) and (grille[i][j] == grille[l][c] or grille[i][j] in decompo):
                    existe[2].append(grille[i][j])
        for k in range(3):
            triplet = []
            if len(existe[k]) == 2:
                for i in [0,1]:
                    for n in existe[k][i]:
                        if n not in triplet:
                            triplet.append(n)
                if triplet != grille[l][c]:
                    existe[k] = False
            else:
                existe[k] = False
        if existe[0]:
            for k in range(9):
                if not grilleFinie[l][k] and grille[l][k] != grille[l][c] and grille[l][k] not in existe[0]:
                    for n in grille[l][k]:
                        if n in grille[l][c]:
                            grille[l][k].remove(n)
        if existe[1]:
            for k in range(9):
                if not grilleFinie[k][c] and grille[k][c] != grille[l][c] and grille[k][c] not in existe[1]:
                    for n in grille[k][c]:
                        if n in grille[l][c]:
                            grille[k][c].remove(n)
        if existe[2]:
            for i in lc:
                for j in cc:
                    if not grilleFinie[i][j] and grille[i][j] != grille[l][c] and grille[i][j] not in existe[2]:
                        for n in grille[i][j]:
                            if n in grille[l][c]:
                                grille[i][j].remove(n)
            
        
def verifier(l=0,c=0):
    global grille,grilleFinie
    if not l and not c:
        for i in range(9):
            for j in range(9):
                if type(grille[i][j]) is list:
                    if len(grille[i][j]) == 1 and grille[i][j][0]:
                        grilleFinie[i][j] = True
                        grille[i][j] = grille[i][j][0]
                else:
                    if grille[i][j] != 0:
                        grilleFinie[i][j] = True
    else:
        if type(grille[l][c]) is list:
            if len(grille[l][c]) == 1 and grille[l][c][0]:
                grilleFinie[l][c] = True
                grille[l][c] = grille[l][c][0]
               
def chercher(ee=0,ite=0):
    global grilleFinie,grille
    iterations = 0
    grilleTest = [[0]*9 for n in range(9)]
    grilleBack = [[0]*9 for n in range(9)]
    cellBack = [0,0,9,[]]
    if ee:
        print(ite,"iter"+"s"*(ite!=1))
    print(" "*(ee-1)+"|"*(ee!=0)+"_ couche",ee,end=" => ")
    while "solution non determinee":
        grilleTest = copie(grille)
        for i in range(9):
            for j in range(9):
                solutions(i,j,iterations)
        for i in range(9):
            for j in range(9):
                if grille[i][j] == []:
                    return False
        if grilleFinie == [[True]*9 for n in range(9)]:
            print(iterations,"iter"+"s"*(iterations!=1))
            affG()
            return True
        if grilleTest == grille:
            grilleBack = copie(grille)
            for i in range(9):
                for j in range(9):
                    if not grilleFinie[i][j] and cellBack[2] > len(grille[i][j]):
                        cellBack = [i,j,len(grille[i][j]),grille[i][j]]
            for n in cellBack[3]:
                grille[cellBack[0]][cellBack[1]] = n
                if chercher(ee+1,iterations):
                    return True
                else:
                    grilleFinie = [[False]*9 for n in range(9)]
                    grille = copie(grilleBack)
                    verifier()
            return False  
        else:
            iterations += 1
    
def copie(l):
    re = [[0]*9 for n in range(9)]
    for i in range(9):
        for j in range(9):
            re[i][j] = l[i][j]
    return re

nouv()
fenetre.mainloop()
