#print("                                          |")"

#region Boucle
activer = True
while activer == True:
    #Choix du programme
    print("============================================")
    print("Quelle partie de leçon veut-tu lire ?")          
    print("1 - Suite explicite")
    print("2 - Suite récurrente")
    print("3 - Suite convergente")
    print("4 - Suite divergente")
    print("5 - Suite arithmétique")
    print("6 - Suite géométrique")
    print("7 - Calculer la somme")
    print("8 - Calculer la raison")
    choix = str(input("Choix : "))
    print()

    #Affiche la partie de leçon choisis
    if choix == "1":
        #print("                                          |")"
        print("SUITE EXPLICITE :")
        print('Les suites "1 par 1"')
        print("Exemple: Un = 3n - 1 ---> V0 = 3x0 - 1 = -1")
    elif choix == "2":
        print("SUITE RECURRENTE :")
        print('Les suite avec "le nombre de avant"')
        print("Exemple: Un + 1 = 4Un - 6 et V0 = 3 --->")
        print("V1 = 4x3 -6 = 6 | V2 = 4x6 -6 = 18")
    elif choix == "3":
        print("SUITE CONVERGENTE :")
        print("Quand une suite augmente/diminue doucement")
        print("vers un nombre, on dit que la suite (Un)")
        print("tant vers ce nombre:\nlim (n --> -inf/+inf) Un = nombre")
    elif choix == "4":
        print("SUITE DIVERGENTE :")
        print("Quand dans une suite tout les résultats")
        print("sont les mêmes ou quelle augmente")
        print("grandement, on dit que la suite (Un)")
        print("diverge vers -inf/+inf :\nlim (n --> inf) Un = +inf/-inf")
    elif choix == "5":
        print("SUITE ARITHMETIQUE :")
        print("Si Un+1 = Un + r: alors Un = U0 + r * n")
        print("- Si r > 0, alors la suite est croissante")
        print("- Si r < 0, alors la suite est décroissante")
    elif choix == "6":
        print("SUITE GEOMETRIQUE :")
        print("Si Un+1 = q * Un: alors Un = U0 * q**n")
        print("Pour U0 > 0 :")
        print("- Si q > 1 alors la suite est croissante")
        print("- Si 0 < q < 1 alors la suite est décroissante")
        print("Pour U0 < 0 :")
        print("- Si q > 1 alors la suite est décroissante")
        print("- Si 0 < q < 1 alors la suite est croissante")
    elif choix == "7":
        print("CALCULER LA SOMME :")
        print("n + 1 = nombre de termes")
        print("Exemple: U0 + ... + U5 = 6\nou U1 + ... + U5 = 5")
        print("Un = chiffre de Umax\n")
        print("Arithmétique: S = (n+1) *  [U0 + Un / 2]")
        print("Géométrique: S = U0 * [1 - q**n+1 / 1 - q]")
    elif choix == "8":
        print("CALCULER LA RAISON :")
        print("Arithmétique: U2 = U1 + (2-1)r --->\nr = U2 - U1 --> Puis équation")
        print("Géométrique: U2 = U1 * q**(2-1) --->\nr = U2 / U1 --> Puis équation")
        print("--> Vérifier ensuite avec les autres valeurs")
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