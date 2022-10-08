#print("                                          |")"

#region Boucle
activer = True
while activer == True:
    #Choix du programme
    print("============================================")
    print("Quelle partie de leçon veut-tu lire ?")          
    print("1 - Tangente à la courbe")
    print("2 - Dérivées")
    print("3 - Formules")
    print("4 - Transformation")
    print("5 - Variations 1")
    print("6 - Variations 2")
    print("7 - Convexe")
    print("8 - Concave")
    print("9 - Point d'inflexion")
    choix = str(input("Choix : "))
    print()

    #Affiche la partie de leçon choisis
    if choix == "1":
        #print("                                          |")"
        print("TANGENTE A LA COURBE :")
        print("y = f'(a) (x - a) + f(a)")
        print("- Généralement, on demande au point\nd'abscisse 0 :")
        print("y = f'(0) (x - 0) + f(0) = f'(0)x + f(0)")
    elif choix == "2":
        print("DERIVEES :")
        print("f(x)    | f'(x)        | sur l'intervalle")
        print("k       | 0            | R")
        print("x       | 1            | R")
        print("x**2    | 2x           | R")
        print("x**3    | 3x**2        | R")
        print("x**n    | nx**n-1      |")
        print("1/x     | -1/x**2      | R / {0}")
        print("√x      | 1/2√x        | ]0;+inf[")
        print("-1/x**2 | 2/x**3       |")
        print("1/2√x   | -1/4x**(3/2) |")
        print("e**x    | e**x         | R")
    elif choix == "3":
        print("FORMULES : ")
        print("(u+v)' = u' + v'")
        print("(ku)'  = ku'")
        print("(uv)'  = u'v + uv'")
        print("(1/u)' = -u' / u**2")
        print("(u/v)' = (u'v - uv') / v**2")
        print("f'(x)  = u'(x) * v'(u(x))")
        print("(√u)'  = u' / 2√u")
        print("(u**n)'  = nu' * u**(n-1)")
        print("(e**u)'  = u' * e**u")
    elif choix == "4":
        print("TRANSFORMATION :")
        print("1 / x**x = x**-x ---> 1 / (x**4 + 3)**2 =")
        print("(x**4 + 3)**-2 ---> nu' * u**(n-1)")
    elif choix == "5":
        #print("                                          |")"
        print("VARIATIONS :")
        print("Ligne 1 [x]: Si intervalle, alors mettre")
        print("intervalle et si il y a les racines,")
        print("alors mettre les les racines")
        print("Ligne 2 [f''(x)]: Si f''(x) a :")
        print("- pas de racines, faire en fonction du")
        print("signe de f''(x). Donc si positif alors")
        print("mettre \"+\", sinon si négatif alrs mettre \"-\"")
        print("- 1 racines, la trouver et remplir\nla ligne 1 et 2 avec")
        print("- 2 racines, la trouver et remplir\nla ligne 1 et 2 avec")
    elif choix == "6":
        print("Ligne 3 [f'(x)]: Selon les signes de la")
        print("ligne 2, mettre les flèches croissantes\net décroissantes")
        print("Ligne 4 [f'(x)]: Si f''(x) n'avait pas de")
        print("racine, alors la faire ici avec un tableau")
        print("de variation normal. Sinon faire en de a")
        print("de f'(x) ou du dernier signe de la ligne 2.")
        print("Ligne 5 [f(x)]: Selon les signes de la")
        print("ligne 4, mettre les flèches croissantes et")
        print("décroissantes. Ne pas oublier de calculer\nf(racines)")
    elif choix == "7":
        print("CONVEXE :")
        print("Une fonction est convexe quand :")
        print("- Le segment de 2 points de la courbe est\nau dessus de la courbe")
        print("- La courbe est au dessus de ses tangentes")
        print("- f'(x) est croissant")
        print("- f''(x) >= 0")
    elif choix == "8":
        print("CONCAVE :")
        print("Une fonction est concave quand :")
        print("- Le segment de 2 points de la courbe est\nau dessous de la courbe")
        print("- La courbe est au dessous de ses tangentes")
        print("- f'(x) est décroissant)")
        print("- f''(x) <= 0")
    elif choix == "9":
        print("POINT D'INFLEXION :")
        print("Point de la courbe où la courbe change de\nconvexité : A(a;f(a))")
    else:
        print("Choix inconnu !")

    #Continuer
    print("\nVeux-tu continuer ?")
    print("1 - Oui")
    print("2 - Non")

    continuer = str(input("Choix : "))

    #Recommence
    if continuer == "1":
        print()

    #Arrête le programme
    else:
        exit()
#endregion