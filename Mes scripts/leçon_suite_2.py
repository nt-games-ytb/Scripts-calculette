#print("                                          |")"

#region Boucle
activer = True
while activer == True:
    #Choix du programme
    print("============================================")
    print("Quelle partie de leçon veut-tu lire ?")          
    print("1 - Exprimer Un+1 en fonction de n")
    print("2 - Sens de variation (méthode 1 et 2)")
    print("3 - Sens de variation (méthode 3 et 4)")
    print("4 - Trouver une conjecture")
    print("5 - Double suite 1")
    print("6 - Double suite 2")
    print("7 - Suite majorée, minorée et bornée")
    print("8 - Démonstration par réccurence 1")
    print("9 - Démonstration par réccurence 2")
    choix = str(input("Choix : "))
    print()

    #Affiche la partie de leçon choisis
    if choix == "1":
        #print("                                          |")"
        print("EXPRIMER Un+1 EN FONCTION DE n :")
        print("Remplace les \"n\" par \"n+1\"")
        print("Exemple: 3n**2 - 2n + 4 --->")
        print("3(n + 1)**2 - 2(n + 1) +4")
        print("-> après développement: 3n**2 + 4n + 5")
    elif choix == "2":
        print("TROUVER LE SENS DE VARIATION :")
        print("Tu as 4 méthodes pour trouver le sens de")
        print("variation d'une suite :")
        print("Méthode 1: Un+1 - Un")
        print("-> Si tu as juste Un, tu calcul Un+1 et tu\nsoustraie")
        print("-> Sinon si tu as Un+1, tu fais une équation")
        print("---> Le signe du résultat sera celui de la\nsuite")
        print("Méthode 2: Un+1 / Un")
        print("-> Si c'est >= 1 alors c'est croissant")
        print("-> Sinon si c'est <= 1 alors c'est décroissant")
        print("-> Sinon si c'est = 1 alors c'est constant")
    elif choix == "3":
        print("TROUVER LE SENS DE VARIATION :")
        print("Méthode 3: Un = f(n)   (sur [0;+inf[)")
        print("-> Tu dérive Un, puis tu trouve le signe")
        print("de la dérivé avec les équations ou le polynome")
        print("Méthode 4: Réccurence")
        print("-> Démontrer par réccurence que Un+1 >= Un")
        print("ou que Un+1 <= Un")
    elif choix == "4":
        print("TROUVER UNE CONJECTURE :")
        print("Trouver une égalité ou une inégalité pour")
        print("une futur démonstration par réccurence")
        print("Exemple: V1 = 5 | V2 = 5 | V3 = 5")
        print("-> Vn = 0 * n + 5 = 5")
    elif choix == "5":
        print("DOUBLE SUITE :")
        print("Soit une suite An+1 et une suite Un")
        print("qui utilse An :")
        print("1 - Trouve Un+1, indique sa raison et son\n1er terme")
        print("Exemple: An+1 = 4000 + 0,8An\net Un = 20000 - An")
        print("-> Un - 20000 = - An ---> An = 20000 - Un")
        print("Un+1 = 20000 - An+1 =")
        print("20000 - (4000 + 0,8(-Un + 20000)) = 0,80Un")
    elif choix == "6":
        print("DOUBLE SUITE 2 :")
        print("2 - Trouver Un")
        print("Exemple: raison = 0,80")
        print("et U0 = 20000 - A0 = 20000 - 7000 = 13000")
        print("Donc Un = 13000 * 0,8**n")
        print("3 - Trouve An")
        print("Exemple: An = 20000 - Un =\n20000 - (13000 * 0,8**n)")
    elif choix == "7":
        print("SUITE MAJOREE, MINOREE ET BORNEE:")
        print("- Majorée par: Nombre >= Un")
        print("- Minorée par: Nombre <= Un")
        print("-> minorée <= Un <= majorée")
        print("- Bornée: majorée et minorée")
    elif choix == "8":
        print("DEMONSTRATION PAR RECCURENCE 1 :")
        print("Soit Pn: \"... (ta conjecture)\"")
        print("Initialisation :")
        print("- Faire U1 (ou U2) et indiquer si s'est")
        print("bien égale à votre conjecture et si\nelle est vrai")
        print("- Si vous l'avez déjà fait alors :")
        print("\"Déjà fait et elle est vrai du rang ... à ...\"")
    elif choix == "9":
        print("DEMONSTRATION PAR RECCURENCE 1 :")
        print("Hérédité :")
        print("- Je suppose que Pn est vrai pour un certains")
        print("rang n, montrons que Pn+1 est vrai :")
        print("- Si on vérifie une égalité, on part de")
        print("Un+1 pour arriver à l'hypothèse de réccurence")
        print("- Si on vérifie une inégalité, on part de")
        print("l'hypothèse de réccurence pour arriver\nà notre conjecture")
        print("Conclusion :")
        print("- Pn est vrai au rang ... à ... et est")
        print("héréditaire, elle est donc vrai pour tout n.")
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