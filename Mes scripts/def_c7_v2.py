#print("                                          |")"

#region Boucle
activer = True
while activer == True:
    #Choix du programme
    print("============================================")
    print("Quelle partie de leçon veut-tu lire ?")          
    print("1 - Onde progressive et mécanique")
    print("2 - Type d'onde")
    print("3 - Directions et propagation des dimensions")
    print("4 - Perturbation, milieu, croissement")
    print("5 - Célérité et retard")
    print("6 - Onde progressive périodique")
    print("7 - Onde doublement périodique")
    print("8 - La période T")
    print("9 - Longueur d'onde λ")
    print("10 - Relation fréquence f, T ou λ")
    print("11 - Formules")
    print("12 - Expression d'un signal sinusoïdale")
    choix = str(input("Choix : "))
    print()

    #Affiche la partie de leçon choisis
    if choix == "1":
        #print("                                          |")"
        print("Définition d'une onde progressive :")
        print("Une onde progressive est à la propagation")
        print("d'une pertubation sans transport globale")
        print("de matière, mais avec transfert d'énergie.\n")
        print("Définition d'une mécanique :")
        print("Une onde mécanique (ex : onde sismique,")
        print("onde acoustique) entraine localement une")
        print("modification de de la position d'un point")
        print("du milieu.")
    elif choix == "2":
        #print("                                          |")"
        print("Type d'onde :")
        print("- Une onde est transversale si la direction")
        print("de la perturbation, en un point de milieu,")
        print("est perpendiculaire à celle de propagation")
        print("de l'onde. Exemples : corde,  vaguelette")
        print("ou echelle de perroquet")
        print("- Une onde est longitudinale si la direction")
        print("de la perturbation en un point de milieu,")
        print("est parallèle à celle de propagation de")
        print("l'onde. Exemples : ressort ou son")
    elif choix == "3":
        #print("                                          |")"
        print("Une onde se propage dans toutes les directions")
        print("offertes par le milieu de propagation.")
        print("Si le milieu, de par sa structure, ne permet")
        print("une propagation que dans une seule direction,")
        print("l'onde est à est à une dimension. Exemples :")
        print("corde, ressort et échelle")
        print("Si la propagation s'effectue dans un plan,")
        print("l'onde est à deux dimensions : Exemples : vaguelette")
        print("L'onde peut-être à trois dimensions.")
        print("Exemples : son")
    elif choix == "4":
        #print("                                          |")"
        print("- Pertuation :")
        print("Une pertubation est une modification locale")
        print("et temporaire d'une des propriétés du milieu")
        print("(température, pression, position d'un point...)")
        print("- Milieu de propagation :")
        print("Les ondes mécaniques ont besoin d'un milieu")
        print("materiel pour se propager mais ne se propage")
        print("pas dans le vide.")
        print("- Croisement de deux ondes : Deux ondes")
        print("peuvent se croiser sans se perturber.")
    elif choix == "5":
        #print("                                          |")"
        print("La célérité v d'une onde est la valeur de")
        print("la vitesse de propagation de la pertubartion.")
        print("Dans le cas d'une onde se propageant dans")
        print("un milieu homogène d'un point A vers un")
        print("point B, v est constante et la perturbation")
        print("observée en A atteint B avec un certain")
        print("retard τ (ou T).")
        print("On peut donc écrire : v = d / τ")
    elif choix == "6":
        #print("                                          |")"
        print("- Onde progressive périodique :")
        print("Une onde progressive est périodique si la")
        print("perturbation est périodique par rapport au")
        print("temps c'est-à-dire si elle se répète")
        print("identiques à elle-même à intervalles de")
        print("temps égaux.")
        print("- Cas particulier onde progressive sinusoïdale :")
        print("Une onde progressive est sinusoïdale si la")
        print("perturbation en un point du milieu décrit")
        print("une fonction sinusoïdale (voir exemple).")
    elif choix == "7":
        #print("                                          |")"
        print("Une onde sinusoïdale présente une double")
        print("périodicité. En effet :")
        print("- en un point du milieu, la perturbation")
        print("se répète identique à elle-même à intervalle")
        print("de temps égaux (périodicité temporelle);")
        print("- à un instant donné, les points d'un dans")
        print("le même état vibratoire sont équidistants")
        print("les uns des autres (périodicité spatiale).")
    elif choix == "8":
        #print("                                          |")"
        print("La période T d'une onde sinusoïdale est la")
        print("plus petite durée au bout de laquelle un")
        print("point du milieu se retrouve dans le même")
        print("état vibratoire, même position et dans")
        print("le même sens.")
    elif choix == "9":
        #print("                                          |")"
        print("La longueur d'onde λ (\"lambda\") est la")
        print("plus  petite distance entre deux points")
        print("qui vibrent en phase au somme (ou 0) au")
        print("même instant.")
        print("Deux points vibrants en phase dont")
        print("séparés d'une distance de λ, 2λ, 3λ, 4λ ou")
        print("nλ avec n entier non nul.")
        print("Deux points en opposition de phase dont")
        print("séparés d'une distance de λ/2, 3λ/2, 5λ/2")
        print("avec n entier non nul.")
    elif choix == "10":
        #print("                                          |")"
        print("La fréquence f d'une onde sinusoïdale est")
        print("de nombre de période par unité de temps")
        print("(la fréquence en Hz est donc le nombre")
        print("perturbation élémentaire par secondes).")
        print("500Hz = 500 vibrations par secondes")
        print("La longueur d'onde λ est une distance")
        print("parcourut par l'onde pendant une période T.")
    elif choix == "11":
        #print("                                          |")"
        print("λ : Longueur d'onde (en m)")
        print("c'est aussi égale à d : distance (en m)")
        print("f : Fréquence (en Hz ou kHz)")
        print("T : période (en s)")
        print("v : célérité de l'onde (en m/s)")
        print("f = 1 / T")
        print("λ = v * T")
        print("v = λ / T = λ * f")
    elif choix == "12":
        #print("                                          |")"
        print("s(t) = A cos(2π/T x t + C) ou s(t)")
        print("= A cos(2π x f x t + C) avec :")
        print("- s(t) : élongation(en m, en V, en Pa,")
        print("etc, selon le phénomène étudié) désigne")
        print("\"un écart par rapport à l'équilibre\" à")
        print("l'instant de date t")
        print("- T : période (en s) de s(t)")
        print("- f = 1 / T : fréquence (en Hz) de s(t)")
        print("- A : amplitude (en m, en V, en Pa, etc,")
        print("selon le phénomène étudié) de s(t).")
        print("C'est l'élongation maximal.")
        print("- C : Phase à l'origine. ")
        print("On choisit - π < C =< π.")
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

    #Arrête le programme
    else:
        exit()
#endregion
#16 lignes
#                                          |Stop Text