#print("                                          |")"

#region Boucle
activer = True
while activer == True:
    #Choix du programme
    print("============================================")
    print("Quelle partie de leçon veut-tu lire ?")          
    print("1 - Objectif d'un dosage")
    print("2 - Dosage par titrage [1]")
    print("3 - Dosage par titrage [2]")
    print("4 - Schéma d'un montage ")
    print("5 - Equation de la réaction")
    print("6 - Résolution d'un problème de titrage")
    print("7 - Repérage de l'équivalence [1]")
    print("8 - Repérage de l'équivalence [2]")
    print("9 - Evolution des quantités de matière")
    print("10 - Faire une demi équation")
    print("11 - Exemple de demi équation")
    choix = str(input("Choix : "))
    print()

    #Affiche la partie de leçon choisis
    if choix == "1":
        #print("                                          |")"
        print("L'objectif d'un dosage est de déterminer")
        print("la concentration en quantité de matière")
        print("(ou en masse) [soit C ou Cm] d'une espèce")
        print("chimique en solution.")
        print("Il existe 2 types de dosage :")
        print("- Le dosage par étalonage où avec une")
        print("solution mère on réalise des solutions")
        print("filles au quelle on va mesure leur")
        print("absobance et ainsi deduire la concentration")
        print("- Le dosage par titrage (voir partie 2)")
    elif choix == "2":
        #print("                                          |")"
        print("Lors d'un dosage par titrage, on réalise")
        print("une réaction chimique pour déterminer la")
        print("concentration de l'espèce titrée. La")
        print("réaction de dosage doit être totale,")
        print("unique (ou univoque) et rapide.")
        print("L'équivalence du dosage se définit comme")
        print("correspondant : au changement de réactifs")
        print("limitant; au moment du titrage où les")
        print("réactifs sont introduits en propotion")
        print("stoechiomètrique.")
    elif choix == "3":
        #print("                                          |")"
        print("L'équivalence d'un dosage doit être")
        print("repérable : elle peut être repérée, par")
        print("exemple, par un changement de teinte du")
        print("milieu réactionnel si l'un des réactifs")
        print("est coloré (de manière différente des")
        print("autres espèces présentes dans le milieu")
        print("réactionnel). Lors d'un titrage direct, la")
        print("réaction de dosage se fait entre le réactif")
        print("dit titré de concentration inconnue et")
        print("recherchée et un réactif dit titrant de")
        print("concentration connue.")
    elif choix == "4":
        #print("                                          |")"
        print("- Burette graduée avec le réactif titrant,")
        print("ressemblant à une croix catho à l'envers")
        print("- Elle même est tenue par une potence")
        print("- Sous la burette, l'erlenmeyer avec dedans")
        print("le reactif titré et un barreau aimanté")
        print("- Lui même sous un agitateur magnétique")
        print("qui ressemble à un rectangle/bloc")
    elif choix == "5":
        #print("                                          |")"
        print("En notant A le réactif titré, B le")
        print("réactif titrant, C et D les produits et")
        print("a, b, c et d les coefficients")
        print("stoechiométriques, l'équation de la réaction")
        print("support d'un titrage direct est :")
        print("a A + b B -> c C + d D")
    elif choix == "6":
        #print("                                          |")"
        print("En notant Vé le volume de solution de")
        print("réactif titrant B versée pour atteindre")
        print("l'équivalence, il suffit d'écrire :")
        print("- A l'équivalence, les réactifs sont")
        print("introduits en proportions stoechiométriques")
        print("donc :")
        print("- n(a)prélevé / a = n(b)versé / b.")
        print("- Ainsi (Ca x Va) / a = (Cb x Vb) / b.")
        print("perturbation en un point du milieu décrit")
        print("une fonction sinusoïdale (voir exemple).")
        """Info supplémentaire : Une fois ces trois lignes écrites, il suffit d'en déduire
l'expression littérale de la concentration cA recherchée de
réactif titrant et, selon la question posée, de la calculer
grâce aux données de l'énoncé et au résultat du titrage
(valeur de Vé) ou d'exploiter cette expression littérale pour
déterminer une concentration en masse, une quantité de
matière ou une masse de A."""
    elif choix == "7":
        #print("                                          |")"
        print("Si le réactif titré A (prélevé et mis dans")
        print("l'erlenmeyer en début de titrage) et/ou le")
        print("réactif titrant B (dans la burette) sont")
        print("colorés de manière différente, l'équivalence")
        print("peut être repéré par un changement de")
        print("teinte du mélange réactionnel dans l'erlenmeyer.")
        print("- Avant l'équivalence, B est limitant et")
        print("totalement consommé. La teinte du mélange")
        print("est celle donnée par A, superposée à celle")
        print("des produits ou des espèces spectatrices.")
    elif choix == "8":
        #print("                                          |")"
        print("- A l'équivalence, le mélange est stoechiométrique")
        print("est incolore, teinte à superposer à celle")
        print("des produits ou des espèces spectatrices.")
        print("- Après l'équivalence, il ne reste plus de")
        print("A. La teinte du mélange est celle donnée")
        print("par B, superposée à celle des produits ou")
        print("des espèces spectatrices.")
        print("- L'équivalence se repère par un changement")
        print("de teinte : couleur de A => couleur de B,")
        print("couleurs à superposer à celle des produits")
        print("ou des espèces spectatrices.")
    elif choix == "9":
        #print("                                          |")"
        print("- Avant l'équivalence :")
        print("n(a) = n(titré) = dimininue")
        print("n(b) = n(titrant = toujours égal à 0")
        print("n(produit) = augmente")
        print("- à l'équivalence :")
        print("n(a) et n(b) = n(titré) et n(titrant) = 0")
        print("n(produit) = stop")
        print("- Après l'équivalence :")
        print("n(a) = n(titré) = toujours égal à 0")
        print("n(b) = n(titrant = augmente")
        print("n(produit) = constant")
    elif choix == "10":
        #print("                                          |")"
        print("- Ecrire les couples (oxydant/réducteur)")
        print("- Ecrire l'équation (ox + e[+] = réd)")
        print("- Vérifie les O dans les red (ajouter des H{2}O (l))")
        print("- Vérifie les H dans les ox (ajouter des H[+] (aq))")
        print("- Calculer les éléctrons ([électrons ox ")
        print("positif - électrons ox negatif] - [électrons")
        print("red positif - électrons red negatif]")
        print("- Surligner les réactifs")
        print("- Récrire l'équation dans l'ordre avec x[]")
        print("Note : {} représente les chiffres en bas")
        print("et [] les chiffre en haut / éléctrons")
    elif choix == "11":
        #print("                                          |")"
        print("Vous pouvez voir ces demi-équation :")
        print("1 - MnO{4}[-](aq) / Mn[2+](aq")
        print("2 - Cu[2+](aq) / Cu(s)")
        print("3 - NO{3}[-](aq) / NO{2}[-](aq)")
        print("4 - NO{3}[-](aq) / NO(g)")
        print("5 - I{2}(aq) / I[-](aq)")
        print("6 - ClO[-](aq) / Cl[-](aq)")
        print("7 - Fe[2+](aq) / Fe(s)")
        print("8 - S{4}O{6}[2-](aq) / S{4}O{6}[2-](aq)")
        print("Il existe encore de nombreuses autres")
        print("demi-équations mais je n'ai pas eu le")
        print("temps de les mettre.")
        choix2 = str(input("Choix : "))
        print()

        if choix2 == "1":
            #print("                                          |")"
            print("MnO{4}[-](aq) / Mn[2+](aq) :")
            print("MnO{4}[-] + e[-] = Mn[2+]")
            print("MnO{4}[-] + e[-] = Mn[2+] + 4H{2}O")
            print("MnO{4}[-] + 8H[+] + e[-] = Mn[2+] + 4H{2}O")
            print("MnO{4}[-] + 8H[+] + 5e[-] = Mn[2+] + 4H{2}O")
            print("- Final : MnO{4}[-](aq) + 8H[+](aq)")
            print("+ 5e[-] = Mn[2+](aq) + 4H{2}O(l)")
        elif choix2 == "2":
            #print("                                          |")"
            print("Cu[2+](aq) / Cu(s) :")
            print("Cu[2+] + e[-] = Cu")
            print("Cu[2+] + 2e[-] = Cu")
            print("- Final : Cu[2+](aq) + 2e[-] = Cu(s)")
        elif choix2 == "3":
            #print("                                          |")"
            print("NO{3}[-](aq) / NO{2}[-](aq) :")
            print("NO{3}[-] + e[-] = NO{2}[-]")
            print("NO{3}[-] + e[-] = NO{2}[-] + H{2}O")
            print("NO{3}[-] + 2H[+] + e[-] = NO{2}[-] + H{2}O")
            print("NO{3}[-] + 2H[+] + 2e[-] = NO{2}[-] + H{2}O")
            print("- Final : NO{3}[-](aq) + 2H[+](aq)")
            print("+ 2e[-] = NO{2}[-](aq) + H{2}O(l)")
        elif choix2 == "4":
            #print("                                          |")"
            print("NO{3}[-](aq) / NO(g) :")
            print("NO{3}[-] + e[-] = NO")
            print("NO{3}[-] + e[-] = NO + 2H{2}O")
            print("NO{3}[-] + 4H[+] + e[-] = NO + 2H{2}O")
            print("NO{3}[-] + 4H[+] + 3e[-] = NO + 2H{2}O")
            print("- Final : NO{3}[-](aq) + 4H[+](aq)")
            print("+ 3e[-] = NO(g) + 2H{2}O(l)")
        elif choix2 == "5":
            #print("                                          |")"
            print("I{2}(aq) / I[-](aq) :")
            print("I{2} + e[-] = I[-]")
            print("I{2} + e[-] = 2I[-]")
            print("I{2} + 2e[-] = 2I[-]")
            print("- Final : I{2}(aq) + 2e[-] = 2I[-](aq)")
        elif choix2 == "6":
            #print("                                          |")"
            print("ClO[-](aq) / Cl[-](aq) :")
            print("ClO[-] + e[-] = Cl[-]")
            print("ClO[-] + e[-] = Cl[-] + H{2}O")
            print("ClO[-] + 2H[+] + e[-] = Cl[-] + H{2}O")
            print("ClO[-] + 2H[+] + 2e[-] = Cl[-] + H{2}O")
            print("- Final : ClO[-](aq) + 2H[+](aq)")
            print("+ 2e[-] = Cl[-](aq) + H{2}O(l)")
        elif choix2 == "7":
            #print("                                          |")"
            print("Fe[2+](aq) / Fe(s) :")
            print("Fe[2+] + e[-] = Fe")
            print("Fe[2+] + 2e[-] = Fe")
            print("- Final : Fe[2+](aq) + 2e[-] = Fe(s)")
        elif choix2 == "8":
            #print("                                          |")"
            print("S{4}O{6}[2-](aq) / S{4}O{6}[2-](aq) :")
            print("S{4}O{6}[2-] + e[-] = S{4}O{6}[2-]")
            print("S{4}O{6}[2-] + e[-] = 2S{4}O{6}[2-]")
            print("S{4}O{6}[2-] + 2e[-] = 2S{4}O{6}[2-]")
            print("- Final : S{4}O{6}[2-](aq) + 2e[-]")
            print("= 2S{4}O{6}[2-](aq)")
        else:
            print("Choix inconnu !")
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
#16 lignes
#                                          |Stop Text