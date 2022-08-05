#print("                                          |")"

#region Boucle
activer = True
while activer == True:
    #Choix du programme
    print("============================================")
    print("Quelle partie de leçon veut-tu lire ?")          
    print("1 - Le chlorure de sodium")
    print("2 - Les caractèristique et la structure cristaline")
    print("3 - Les différents réseaux")
    print("4 - La compacité")
    print("5 - Propriétés macroscopiques")
    print("6 - Représentation en perspective cavalière")
    choix = str(input("Choix : "))
    print()

    #Affiche la partie de leçon choisis
    if choix == "1":
        #print("                                          |")"
        print("LE CHLORURE DE SODIUM :")
        print("Le sel ou le chlorure de sodium de formule")
        print("NaCl est présent sous sa forme solide dans")
        print("certaines roches ou provient de")
        print("l'évaporation de l'eau de mer.")
        print("Au niveau microscopique, le chlorure de")
        print("sodium solide est constitué d'un empilement")
        print("régulier d'ions sodium (Na+) et d'ions")
        print("chlorure (Cl-) : c'est l'état cristallin.")
        print("Au niveau macroscopique, les cristaux de")
        print("chlorure de sodium ont une forme cubique,")
        print("similaire à l'organisation microscopique.")
    elif choix == "2":
        #print("                                          |")"
        print("LES CARACTERISTIQUES ET LA STRUCTURE CRISTALINE :")
        print("Une structure cristalline est définie par")
        print("la répétition périodique dans l'espace ")
        print("d'une structure élémentaire appelée maille")
        print("élémentaire. Un cristal est caractérisé par :")
        print("- La forme géométrique de la maille")
        print("- La nature des entités qui le constitue,")
        print("généralement un atome, une molécule ou des ions")
        print("- La position des entités chimiques dans la maille")
    elif choix == "3":
        #print("                                          |")"
        print("LES DIFFERENTS RESEAUX :")
        print("Les cristaux les plus simples sont constitués")
        print("d'un réseau de mailles qui ont la géométrie")
        print("d'un cube : on parle de mailles cubiques.")
        print("La position des entités dans la maille")
        print("élémentaire permet de distinguer différents")
        print("types de réseaux cubiques :")
        print("- Cubique simple :")
        print("Les entités se situent aux 8 sommets du cube")
        print("On a : 8 x (1/8) = 1")
        print("On a 1 entité par maille")
        print("- Cubique à faces centrées :")
        print("Les entités si situent aux 8 sommets du")
        print("cube et au centre des 6 faces")
        print("On a : 8 x (1/8) + 6 x (1/2) = 4")
        print("On a 4 entités par maille")
    elif choix == "4":
        #print("                                          |")"
        print("LA COMPACITE :")
        print("Ces deux réseaux se différencient par le")
        print("taux d'occupation de la maille élémentaire")
        print("par les entités. Il est possible de")
        print("calculer ce taux d'occupation grâce à un")
        print('calcul de compacité. La compacité "c"')
        print("d'une structure cristalline est un nombre")
        print("compris entre 0 et 1 donné par la relation :")
        print("c = volume des entites/volume de la maile")
        print("- Cubique simple :")
        print("c = Vsphere / Vcube -> avec a = 2 x r")
        print("= (4/3 x π x r**3) / a**3 = 0,52")
        print("Taux d'occupation : 52%")
        print("- Cubique à faces centrées :")
        print("c = 4 x (Vsphere/Vcube)")
        print("-> avec a = (4 x r) / √2")
        print("= (4 x 4/3 x π x r**3) / a**3 = 0,74")
        print("Taux d'occupation : 74%")
    elif choix == "5":
        #print("                                          |")"
        print("PROPRIETES MACROSCOPIQUES :")
        print("La structure de la maille (celle ")
        print("microscopique) conditionne certaines propriétés")
        print("macroscopiques, dont la masse volumique.")
        print('La masse volumique "p" est le quotient')
        print("de la masse des entités d'une maille sur")
        print("son volume en Kg/m**3 ou Kg/L :")
        print("p = m.maille/Vmaille = m des entités/Vmaille")
        print("- Cubique simple :")
        print("Multiplicité : On a 1 entité par maille")
        print("p = m.entité / a3")
        print("- Cubique à faces centrées :")
        print("Multiplicité : On a 4 entité par maille")
        print("p = (4 x m.entité) / a3")
    elif choix == "6":
        #print("                                          |")"
        print("REPRESENTATION EN PERSPECTIVE CAVALIERE :")
        print("a = longueur d'un côté")
        print("alpha = degré d'une diagonale")
        print("k = coefficient de perspective")
        print("a x k = longueur d'une diagonale")
        print("- Cubique simple :")
        print("a / 2 = r | a = 2 x r")
        print("- Cubique face centré :")
        print("D = 4 x r | D**2 = a**2 + a**2 = 2a**2")
        print("a√2 = 4 x r | ^-- Théorème de pythagore")
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