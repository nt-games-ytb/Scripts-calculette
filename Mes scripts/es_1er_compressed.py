from math import *
from kandinsky import *
from ion import *
wien = 0.0028989
c = 300000000
print("Bienvenue dans ES_1er.py créer par nt games !")
print("")
activer = True
while activer == True:
    print("Quel matière veut-tu ?")
    print("1 - Physique-Chimie | 2 - SVT")
    choixMatière = str(input("Choix : "))
    print("")
    if choixMatière == "1":
        print("Que veut-tu faire ?")
        print("1 - Température et couleur")
        print("2 - Loi de Wien")
        print("3 - Masse et énergie")
        print("4 - Univers")
        print("5 - Etres-vivants")
        print("6 - Terre")
        print("7 - Réactions nucléaire")
        print("8 - Fusion")
        print("9 - Fission")
        choixPhysique = str(input("Choix : "))
        print("")
        if choixPhysique == "1":
            print("Froide = Rouge | Chaude = Bleu")
        if choixPhysique == "2":
            print("Lambda max = 2,8989 * 10**-3 / T")
            print("T = K = °c + 273.15 | Lambda max en m")
            print("")
            print("Que veut-tu faire ?")
            print("1 - Calcul Lambda max")
            print("2 - Calcul T")
            print("3 - Retour")
            choixWien = str(input("Choix : "))
            print("")
            if choixWien == "1":
                T = float(input("T : "))
                resultat = wien / T
                print(str(wien) + " / " + str(T) + " = " + str(resultat) + " m")
            if choixWien == "2":
                lambdaMax = float(input("Lambda max : "))
                resultat = wien / lambdaMax
                temperature = resultat + 273.15
                print(str(wien) + " / " + str(lambdaMax) + " = " + str(resultat) + "°K")
                print(str(resultat) + " + 273,15" + " = " + str(temperature) + "°c")
        if choixPhysique == "3":
            print("Masse et énergie : E = m * c**2")
            print("m = Masse perdu = E / c**2 [en Kg]")
            print("c = Vitesse de la lumière = 3,00 * 10**8 [en m/s]")
            print("E = Energie libéré = P * t [en J]")
            print("P = Puissance rayonné = E / t [en W]")
            print("t = temps [en s]")
            print("")
            print("Que veut-tu faire ?")
            print("1 - Calcul E = mc²")
            print("2 - Calcul m")
            print("3 - Calcul E")
            print("4 - Calcul P")
            print("5 - Retour")
            choixEnergie = str(input("Choix : "))
            print("")
            if choixEnergie == "1":
                m = float(input("m : "))
                resultat = m * c**2
                print(str(m) + " * (3,00 * 10**8)**2 = " + str(resultat) + " J")
            if choixEnergie == "2":
                E = float(input("E : "))
                resultat = E / c**2
                print(str(E) + " / (3,00 * 10**8)**2 = " + str(resultat) + " Kg")
            if choixEnergie == "3":
                P = float(input("P : "))
                t = float(input("t : "))
                resultat = P * t
                print(str(P) + " * " + str(t) + " = " + str(resultat) + " J")
            if choixEnergie == "4":
                E = float(input("E : "))
                t = float(input("t : "))
                resultat = E / t
                print(str(E) + " / " + str(t) + " = " + str(resultat) + " W")
        if choixPhysique == "4":
            print("L'univers est composée de 118 éléments")
            print("chimiques différents mais principalement")
            print("d'hydrogène et d'Helium.")
        if choixPhysique == "5":
            print("Les êtres-vivants sont composée")
            print("principalement d'oxygène, de carbone,")
            print("d'hydrogène et d'azote.")
        if choixPhysique == "6":
            print("La terre est composée de 94 éléments")
            print("chimique naturel et 24 artificielles mais")
            print("mais principalement d'oxygène, de fer")
            print("de silicium, d'aluminium et de calcium.")
        if choixPhysique == "7":
            print("Au cours d'une réaction nucléaire, il y a")
            print("conservation des nucléons A et des")
            print(" protons Z.")
            print("Z = protons = numéro atomique")
            print("n = neutons")
            print("Nucléons = protons + neutrons")
        if choixPhysique == "8":
            print("Dans la fusion, les éléments chimique")
            print("légers (petit Z) réagissent pour former des")
            print("éléments chimique lourd (grand Z).")
            print("Les noyaux des atomes de la centaine")
            print("d'éléments chimiques stables résultent de")
            print("la fusion au sein des étoiles à partir de")
            print("l'hydrogène initial.")
            print("Exemple : [2;1]H + [3;1]H --> [4;2]He")
            print("+ [1;0]n")
        if choixPhysique == "9":
            print("La fission se crée quand un neutron rentre")
            print("en colision avec un gros atome pour former")
            print("plusieurs petit atome.")
            print("Exemple : [1;0]n + [235;92]U --> [94;38]Sr")
            print("+ [139;54]Xe + 3[1;0]n")
    if choixMatière == "2":
        print("Que veut-tu faire ?")
        print("1 - Albédo")
        print("2 - Révision du DS1")
        print("3 - Correction du DS1")
        print("4 - Révision du DS2")
        choixPhysique = str(input("Choix : "))
        print("")
        if choixPhysique == "1":
            print("Albedo = (Puissance solaire réfléchie) /")
            print("(Puissance solaire reçue)")
            print("")
            print("Veut-tu le calculer ?")
            print("1 - Oui | 2 - Non")
            choixAlbedo = str(input("Choix : "))
            print("")
            if choixAlbedo == "1":
                réfléchie = float(input("Puissance solaire réfléchie : "))
                reçu = float(input("Puissance solaire reçue : "))
                resultat = réfléchie / reçu
                print(str(réfléchie) + " / " + str(reçu) + " = " + str(resultat) + " = " + str(resultat * 100) + "%")
        if choixPhysique == "2":
            activerRevision1 = False
            print("P = énergie = puissance radiactive")
            print("solaire = 3,85 * 10**26 W")
            print("")
            print("Les variations saisonières de la")
            print("température dépendent de la position du point")
            print("étudié par rapport au zénith qui modifie")
            print("l'angle d'incidence des rayons solaire")
            print("captés et donc la puissance solaire reçue.")
            print("")
            print("La puisssance capté augmente donc du matin")
            print("vers la mi journée, puis diminue au cours")
            print("du reste de la journée, ce qui fait")
            print("augmenter puis diminuer la température.")
            print("         Page 2 (Appuyer sur --->)         ")
            while activerRevision1 == False:
                    if keydown(KEY_RIGHT):
                        activerRevision1 = True
                        print("")
                        print("Bilan :")
                        print("La puissance radiactive saloire reçue du")
                        print("soleil par une surface plane dépend de")
                        print("l'aire de la surface de la zone étudiée et")
                        print("de l'angle d'incidence des rayons solaires")
                        print("frappant cette surface. La puissance solaire")
                        print("reçue par unité de surface dépend donc :")
                        print("de l'heure (variations diurnes), du moment")
                        print("de l'année (variations saisonnière) et de")
                        print("la latitude (zonation climatique).")
        if choixPhysique == "3":
            activerDS1Page1 = False
            print("La puissance solaire reçu est")
            print("proportionelle à la surface. En un point du")
            print("globe, la puissance reçu du Soleil ne")
            print("dépend pas de la longitude.")
            print("")
            print("Phénomène de variation :")
            print("Diurne : Rotation de la terre sur elle même")
            print("Saisonnière : Inclinaison de l'axe de")
            print("rotation de la Terre et révolution autour")
            print("du Soleil")
            print("Climatique : Inclinaison de l'axe de")
            print("rotation de la Terre et forme sphérique de")
            print("la Terre")
            print("         Page 2 (Appuyer sur --->)         ")
            while activerDS1Page1 == False:
                    if keydown(KEY_RIGHT):
                        activerDS1Page1 = True
                        activerDS1Page2 = False
                        print("")
                        print("Les différents climats de la planète :")
                        print("La puissance solaire envoyé sur Terre est")
                        print("constante et ne dépend que de la distance")
                        print("entre la Terre et le Soleil, c'est la")
                        print("constante solaire. Par contre, la Terre")
                        print("étant sphérique, l'angle d'incidence des")
                        print("rayons solaire modifie la surface de la")
                        print("tache éclairée au niveau du sol selon sa")
                        print("latitude et donc de la puissance capté par")
                        print("m**2 par celle-ci. Cette inégale")
                        print("répartition de l'énergie solaire captée au")
                        print("sol est responsable de la zonation")
                        print("         Page 3 (Appuyer sur --->)         ")
                        while activerDS1Page2 == False:
                                if keydown(KEY_RIGHT):
                                    activerDS1Page2 = True
                                    print("")
                                    print("climatique constaté basée sur les")
                                    print("variations de T°.")
        if choixPhysique == "4":
            activerRevision2Page1 = False
            print("Les plantes verte absorbent de l'énergie")
            print("solaire qui est utilisé pour produire de la")
            print("matière consommé et utilisé par d'autres")
            print("êtres vivants.")
            print("")
            print("Autotrophe : parties vertes d'une plante")
            print("(utilise de l'eau, des sels minéraux et de")
            print("la lumière)")
            print("Hétérotrophe : parties non chlorophylliennes")
            print("d'une plante et les autres êtres vivants")
            print("[ex : humains] (utilise de l'eau, des sels")
            print("minéraux, de la lumière et des matières")
            print("organiques)")
            print("         Page 2 (Appuyer sur --->)         ")
            while activerRevision2Page1 == False:
                    if keydown(KEY_RIGHT):
                        activerRevision2Page1 = True
                        activerRevision2Page2 = False
                        print("")
                        print("La chlorophylle absorbe le bleu et le rouge")
                        print("(magenta) ce qui lui donne une couleur")
                        print("verte. Les longeurs d'ondes absorbées par")
                        print("la chlorophylle sont réellement les")
                        print("longueurs d'onde actives pour la")
                        print("photsynthèse.")
                        print("La photosynthèse est le processus   ")
                        print("bioénergétique qui permet à des organismes")
                        print("de synthétiser la matière organique en")
                        print("utilisant l'énergie lumineuse, l'eau et")
                        print("le CO(2).")
                        print("")
                        print("         Page 3 (Appuyer sur --->)         ")
                        while activerRevision2Page2 == False:
                                if keydown(KEY_RIGHT):
                                    activerRevision2Page2 = True
                                    print("")
                                    print("Bilan énergétique de la photosynthèse :")
                                    print("6CO(2) + 6H(2)O --> (Energie lumineuse")
                                    print("[56 000 KJ]) --> C(6)H(12)O(6)")
                                    print("(1 mole de glucose [2 840 KJ]) + 6O(2)")
                                    print("--> Amidon")
    else:
        print("Erreur sur le choix de la commande !")
    print("")
    print("Veux-tu continuer ?")
    print("1 - Oui")
    print("2 - Non")
    continuer = str(input("Choix : "))
    if continuer == "1":
        print("")
    else:
        exit()