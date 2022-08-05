#print("                                          |")"

#region Boucle
activer = True
while activer == True:
    #Choix du programme
    print("============================================")
    print("Quelle partie de leçon veut-tu lire ?")          
    print("1 - Modèle ondulatoire de la lumière")
    print("2 - Modèle particulaire de la lumière 1")
    print("3 - Modèle particulaire de la lumière 2")
    print("4 - Quantification des niveaux 1")
    print("5 - Quantification des niveaux 2")
    choix = str(input("Choix : "))
    print()

    #Affiche la partie de leçon choisis
    if choix == "1":
        #print("                                          |")"
        print("Une onde électromagnétique monochromatique")
        print("(ou radiation) correspond une vibration")
        print("caractérisée par sa période T ou sa fréquence")
        print("noté v telle que nu = 1/T, qui se propage")
        print("dans le vide à la célérité c = 3,00*10**8 m/s")
        print("sans transport de matière mais avec transfert")
        print("d'énergie. La longueur d'onde λ dans le") 
        print("vide (ou dans l'air) d'une radiation")
        print("monochromatiqueest la distance parcourue")
        print("par l'onde électromagnétique dans le vide")
        print("pendant la période T de la vibration. Elle")
        print("est reliée à la fréquence v de l'onde par")
        print("la relation : λ(en m) = C(en m/s)/v (en Hz)") 
    elif choix == "2":
        #print("                                          |")"
        print("Les transferts d'énergie entre matière et")
        print("lumière sont discontinus ou quantifiés :")
        print("ils ne peuvent se faire que par \"paquets\"")
        print("d'énergie contenant chacun une énergie")
        print("bien déterminée. En physique, un paquet")
        print("d'énergie contenant la plus petite énergie")
        print("échangeable est appelé un quantum. Un")
        print("quantum d'énergie lumineuse est appelé un")
        print("photon.")
    elif choix == "3":
        #print("                                          |")"
        print("L'énergie d'un photon ne dépend que")
        print("de la fréquence de la radiation qui le")
        print("transporte ou, ce qui revient au même, de")
        print("sa longueur d'onde dans le vide. On peut")
        print("modéliser la lumière par un déplacement de")  
        print("particules de masse nulle, les photons, ce")
        print("propageant dans le vide à la célérité c = 3,00*10**8 m/s.")
        print("L'énergie d'un photon associé à une radiation")
        print("de fréquence v, est donnée par la relation :")
        print("|△E| = hv (formule de Planck) -> h désigne")
        print("une constante universelle appelée constante")
        print("de Planck : h = 6,63 * 10**–34  J/s. ")
    elif choix == "4":
        #print("                                          |")"
        print("À chaque répartition des électrons sur les")
        print("couches électroniques correspond un niveau.")
        print("d'énergie de l'atome. Les niveaux d'énergie")
        print("d'un atome ont des valeurs bien déterminées,")
        print("caractéristiques de l'atome. Lorsque")
        print("l'atome est à son niveau d'énergie le plus")
        print("as, on dit qu'il est dans son état")
        print("fondamental. Sinon, on dit qu'il est dans")
        print("un état excité. Un changement de niveau")
        print("s'appelle une transition qui :")
    elif choix == "5":
        #print("                                          |")"
        print("- est symbolisée par une flèche droite")
        print("orientée vers le bas lorsque l'atome passe")
        print("d'un niveau d'énergie supérieur vers un")
        print("niveau inférieur et s'accompagne alors")
        print("d'une émission d'un rayonnement, un photon,")
        print("représenté par une flèche ondulée sortante : (voir a. de la figure ci-contre)")
        print("- est symbolisée par une flèche droite")
        print("orientée vers le haut lorsque l'atome") 
        print("passe d'un niveau d'énergie inférieur vers") 
        print("un niveau supérieur et s'accompagne alors")
        print("d'une absorption d'un photon représenté")
        print("par une flèche ondulée entrante.")
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
#16 lignes
#                                          |Stop Text