#Info :
#Max 16 lignes
#Dernière page 11 lignes (print)

#Modules
from math import *
from kandinsky import *
from ion import *

#Chiffre important
wien = 0.0028989
c = 300000000

#Introduction
print("Bienvenue dans triche_es_pc.py créer par nt games !\n")

activer = True
while activer == True:

    #Choix
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
    print("10 - Radioactivité")
    print("11 - Demi-vie")
    choixPhysique = str(input("Choix : "))
    print("")

    #Température et couleur
    if choixPhysique == "1":
        print("Froide = Rouge | Chaude = Bleu")

    #Loi de Wien
    elif choixPhysique == "2":
        print("Lambda max = 2,8989 * 10**-3 / T")
        print("T = K = °c + 273.15 | Lambda max en m (10**3 mm) (10**6 µm) (10**9 nm)")
        print("")

       #Choix
        print("Que veut-tu faire ?")
        print("1 - Calcul Lambda max")
        print("2 - Calcul T")
        print("3 - Retour")
        choixWien = str(input("Choix : "))
        #print("")

        #Calcul Lambda max
        if choixWien == "1":
            T = float(input("T : "))
            resultat = wien / T
            print(str(wien) + " / " + str(T) + " = " + str(resultat) + " m")
 
        #Calcul T
        if choixWien == "2":
            lambdaMax = float(input("Lambda max : "))
            resultat = wien / lambdaMax
            temperature = resultat + 273.15
            print(str(wien) + " / " + str(lambdaMax) + " = " + str(resultat) + "°K")
            print(str(resultat) + " + 273,15" + " = " + str(temperature) + "°c")

    #Masse et energie
    elif choixPhysique == "3":
        print("Masse et énergie : E = m * c**2")
        print("m = Masse perdu = E / c**2 [en Kg]")
        print("c = Vitesse de la lumière = 3,00 * 10**8 [en m/s]")
        print("E = Energie libéré = P * t [en J]")
        print("P = Puissance rayonné = E / t [en W]")
        print("t = temps [en s]")
        print("")

        #Choix
        print("Que veut-tu faire ?")
        print("1 - Calcul E = mc²")
        print("2 - Calcul m")
        print("3 - Calcul E")
        print("4 - Calcul P")
        print("5 - Retour")
        choixEnergie = str(input("Choix : "))
        #print("")

        #Calcul E = mc²
        if choixEnergie == "1":
            m = float(input("m : "))
            resultat = m * c**2
            print(str(m) + " * (3,00 * 10**8)**2 = " + str(resultat) + " J")

        #Calcul m
        if choixEnergie == "2":
            E = float(input("E : "))
            resultat = E / c**2
            print(str(E) + " / (3,00 * 10**8)**2 = " + str(resultat) + " Kg")

         #Calcul E
        if choixEnergie == "3":
            P = float(input("P : "))
            t = float(input("t : "))
            resultat = P * t
            print(str(P) + " * " + str(t) + " = " + str(resultat) + " J")

        #Calcul m
        if choixEnergie == "4":
            E = float(input("E : "))
            t = float(input("t : "))
            resultat = E / t
            print(str(E) + " / " + str(t) + " = " + str(resultat) + " W")

    #Univers
    elif choixPhysique == "4":
        #print("                                          |")"
        print("L'univers est composée de 118 éléments")
        print("chimiques différents mais principalement")
        print("d'hydrogène et d'Helium.")

    #Etre vivants
    elif choixPhysique == "5":
        #print("                                          |")"
        print("Les êtres-vivants sont composée")
        print("principalement d'oxygène, de carbone,")
        print("d'hydrogène et d'azote.")

    #Terre
    elif choixPhysique == "6":
        #print("                                          |")"
        print("La terre est composée de 94 éléments")
        print("chimique naturel et 24 artificielles mais")
        print("mais principalement d'oxygène, de fer")
        print("de silicium, d'aluminium et de calcium.")

    #Réaction nucléaire
    elif choixPhysique == "7":
        #print("                                          |")"
        print("Au cours d'une réaction nucléaire, il y a")
        print("conservation des nucléons A et des")
        print("protons Z.")
        print("Z = protons = numéro atomique")
        print("n = neutons")
        print("Nucléons = protons + neutrons")

    #Fusion
    elif choixPhysique == "8":
        #print("                                          |")"
        print("Dans la fusion, les éléments chimique")
        print("légers (petit Z) réagissent pour former des")
        print("éléments chimique lourd (grand Z).")
        print("Les noyaux des atomes de la centaine")
        print("d'éléments chimiques stables résultent de")
        print("la fusion au sein des étoiles à partir de")
        print("l'hydrogène initial.")
        print("Exemple : [2;1]H + [3;1]H --> [4;2]He")
        print("+ [1;0]n")

    #Fission
    elif choixPhysique == "9":
        #print("                                          |")"
        print("La fission se crée quand un neutron rentre")
        print("en colision avec un gros atome pour former")
        print("plusieurs petit atome.")
        print("Exemple : [1;0]n + [235;92]U --> [94;38]Sr")
        print("+ [139;54]Xe + 3[1;0]n")

    #Radioactivité
    elif choixPhysique == "10":
        #print("                                          |")"
        print("Certains noyaux (ayant trop de neutrons,")
        print("de protons ou de nucléons) sont instables.")
        print("Ils se désintègrent mais on ne sait pas")
        print("quand, c'est la radioactivité.")
        print("Exemple : [238;32]U --> [234;90]Th + [4;2]He")
        print("(comparer au fusion et au fission,")
        print("le noyaux se divise tout seul)")

    #Demi-vie
    elif choixPhysique == "11":
        #print("                                          |")"
        print("La demi-vie (t1/2) d'un noyaux radioactif")
        print("est la durée nécessaire pour que la moitié")
        print("des noyaux initialement présents dans un")
        print("échantillon macroscopique se soit")
        print("désintégrée. Cette demi-vie est")
        print("caractèristique du noyaux radioactif.")
        print("Exemple :")
        print("- Carbone 14 (datation de cadavre) :")
        print("t1/2 = 5730 ans")
        print("- Iode 123 (Imagerie médical) : t1/2 = 13,2h")
        print("- Uranium 238 (réacteurs nucléaires) :")
        print("t1/2 = 4,5 * 10**9 ans")

    #Commande invalide
    else:
        print("Erreur sur le choix de la commande !")

    #Continuer
    print("")
    print("Veux-tu continuer ?")
    print("1 - Oui")
    print("2 - Non")

    continuer = str(input("Choix : "))

    #Recommence
    if continuer == "1":
        print("")

    #Arrête le programme
    else:
        exit()

