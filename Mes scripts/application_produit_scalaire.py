#print("                                          |")"

#region Boucle
activer = True
while activer == True:
    #Choix du programme
    print("============================================")
    print("Quelle partie de leçon veut-tu lire ?")
    print("1 - Probabilitées")
    print("2 - Equations de droite")
    print("3 - Equations de cercle")
    print("4 - Théorème d'Ai Kashi")
    print("5 - Théorème de la médiane")
    print("6 - Autres")
    print("7 - Utilisations")
    choix = str(input("Choix : "))
    print()

    #Affiche la partie de leçon choisis
    if choix == "1":
        #print("                                          |")"
        print("PROBABILITE :")
        print("- Espérance :")
        print("E(x) = p1*x1 + p2*x2 + ... + pn*xn = somme pi*xi")
        print("- Variance :")
        print("V(x) = p1(x1-E(x))**2 + p2(x2-E(x))**2 +")
        print(" ... + pn(xn-E(x))**2 = somme pi(xi-E(x))**2")
        print("- Ecart type :")
        print("sigma(x) = √(V(x))")
        print("- Loi de probabilité :")
        print("Faire un tableau de ligne \"X\" et \"P(x=X)\"")
        print("avec en 1ère ligne les issues et en 2ème,")
        print("le pourcentage que sa puisse se produire.")
    elif choix == "2":
        #print("                                          |")"
        print("EQUATION DE DROITE :")
        print("- Un vecteur directeur est un vecteur avec")
        print("même direction et même sens ---> C'est lui")
        print("qui dirige une droite")
        print("- Un vecteur orthogonal est un vecteur perpendiculaire")
        print("- Un vecteur collinéaire est un vecteur parallèle")
        print("- Un vecteur normal est un vecteur orthogonal")
        print("au vecteur directeur ---> vecteur")
        print("perpendiculaire au vecteur directeur")
        print("- Coordonnées d'un vecteur = c(nombre de case en x pour aller et à vers b;")
        print("nombre de case en y pour aller et à vers b)")
        print("---> donc vecteur directeur : u(a;b) --> équation cartésienne : ax + by + c = 0")
        print("---> donc vecteur normal : u(a;b) --> équation cartésienne : u * v = ax + by = 0")
    elif choix == "3":
        #print("                                          |")"
        print("EQUATION DE CERCLE :")
        print("- Cercle de centre A(xa;ya) et de rayon r :")
        print("r**2 = (x-xa)**2 + (y-ya)**2")
        print("Demonstration :")
        print("Tout point M(x;y) appartient au cercle de")
        print("centre A(xa;ya) et de rayon r si et")
        print("seulement si AM**2 = r**2")
    elif choix == "4":
        #print("                                          |")"
        print("THEOREME D'AI KASHI :")
        print("Minuscule les longueurs|Majuscule les angles")
        print("Dans un triangle ABC, on a :")
        print("a**2 = b**2 + c**2 - 2bc * cos(A)")
        print("Soit aussi :")
        print("AB * AC = AB * AC * cos(A) = bc * cos (A)")
        print("-> AB * AC = 1/2(AB**2 + AC**2 - BC**2)")
        print("= 1/2(b**2 + c**2 - a**2)")
        print("Donc : 1/2(b**2 + c**2 - a**2) = bc*cos(A)")
        print("Soit : a**2 = b**2 + c**2 - 2bc * cos(A)")
    elif choix == "5":
        #print("                                          |")"
        print("THEOREME DE LA MEDIANE :")
        print("Soit A et B, deux points et I milieu de")
        print("[AB] alors pour tout M du plan on a :")
        print("MA**2 + MB**2 = (2 * MI**2) + (AB**2 / 2)")
        print("MA * MB = MI**2 - (AB/4)")
        print("L'emsemble des points M vérifiant l'égalité")
        print("MA * MB = 0 est le cercle de diamètre [AB].")
        print("Un point M distinct de A et B, appartient ")
        print("au cercle de diamètre [AB] si et seulement")
        print("si le triangle ABM est rectangle en M.")
        print("MA * MB = 0 si et seulement si les vecteurs")
        print("MA et MB sont orthogonaux.")
    elif choix == "6":
        #print("                                          |")"
        print("AUTRES :")
        print("- Vecteurs directeurs :")
        print("AB = (xb-xa;yb-ya)")
        print("- Vecteurs normal :")
        print("(xa;ya) * (xb;yb)= xa*xb + ya*yb = 0")
        print("u(x;y) / n(y;-x)")
        print("- Equation de droite avec vecteur normal :")
        print("d = ax + by + c")
        print("-> Pour trouver c : avoir 1 point et")
        print("remplacer ses coordonnées dans l'équation,")
        print("puis la résoudre et vous trouverez c.")
        print("- Calculer les coordonées du milieu d'un")
        print("segment en connaissant les coordonnées des 2 points :")
        print("I(xa+xb /2 ; ya+yb /2)")
        print("- Coefficiant directeur d'une droite :")
        print("u(-b;a) | Exemple : 2x-5y+3=0 -> u=(5;2)")
    elif choix == "7":
        #print("                                          |")"
        print("UTILISATIONS :")
        print("- Coordonnées du centre et du rayon d'un cercle :")
        print("-> Utilise la formule de l'équation de cercle")
        print("en changeant xa et ya par le x et le y")
        print("diviser par 2 et ajouter un -(le nombre **2)")
        print("I (centre) sera égale (xa;ya) et R la √(des nombres pas entre paranthèse ensemble)")
        print("Et l'inverse à si on a un centre et un rayon")
        print("- Calculer des angles :")
        print("théorème d'Ai Kashi -> prendre la formule")
        print("de base puis la mettre comme ça : a = l'inverse de l'angle calculé")
        print("cos (A) = (-a**2 + b**2 + c**2) / 2bc")
        print("puis faire arcos du résultat")
        print("- Calculer CI (I milieu de [AB]) : C = M")
        print("-> utilise la formaule de la médiane,")
        print("remplace tout et exclue CI -> AC**2 + BC**2 - (AB**2 / 2) = 2CI**2 ")
        print("vecteur directeur de d : u(-b;a)")
        print("- Point d'intersection : multiplie d et")
        print("d' pour quelle soit égale et isole y et x")
    else:
        print("Choix inconnu !")

    #Continuer
    print("\nVeux-tu continuer ? 1 - Oui | 2 - Non")

    continuer = str(input("Choix : "))

    #Recommence
    if continuer == "1":
        print()

    #Arrête le programme
    else:
        exit()
#endregion