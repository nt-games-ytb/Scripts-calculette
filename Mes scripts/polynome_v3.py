########################################################################################
#                                                                                      #
#  PPP  ooo  L    Y Y  N   N  ooo  M   M  EEE   V V  333                               #
#  P P  o o  L    Y Y  NN  N  o o  MM MM  E     V V    3                               #
#  PPP  o o  L    YYY  N N N  o o  M M M  EE    V V  333                               #
#  P    o o  L     Y   N  NN  o o  M   M  E     V V    3                               #
#  P    ooo  LLL   Y   N   N  ooo  M   M  EEE .  V   333 by nt games and Mael | 1er G3 #
#                                                                                      #
########################################################################################

#print("                                          |")"

#region Import
import math
#endregion

#region Variables
a = 0
b = 0
c = 0
alpha = 0
beta = 0
delta = 0
x1 = 0
x2 = 0
somme = 0
produit = 0
#endregion

#Fonction
def développé():
    print("Forme développé = ax**2 + bx + c")
    a = int(input("A : "))
    b = int(input("B : "))
    c = int(input("C : "))

    if a == 0:
        print("Ce n'est pas un polnyônme du 2nd degré !\nTu peux la résoudre de tête !")

    else:
        #Forme développé
        print("Forme développé = " + str(a) + "x**2 +" + str(b) + "x +" + str(c) + "\n")
        
        #region Signe
        signe = ""
        if a >= 0:
            signe = "+"
        else:
            signe = "-"
        #endregion

        #region Forme Cannonique
        #Alpha
        alpha = (-b) / (2*a)
        print("Alpha = " + str(alpha)  + " ---> -b / 2a = -" + str(b) + " / 2*" + str(a))

        #Bêta
        beta = -((b**2) - (4*a*c)) / (4*a) #Technique 2
        print("Bêta = " + str(beta) + " ---> - (b**2 - 4ac) / 4a = - (" + str(b) + "**2 - 4*" + str(a) + "*" + str(c) + ") / 4*" + str(a) + " aussi égal à : a * alpha**2 + b * alpha + c")

        #region Old
        '''if alpha < 0 and beta < 0:
            print("Forme canonique = " + str(a) + "(x+" + str(-alpha) + ")**2-" + str(-beta))
        elif alpha >= 0 and beta >= 0:
            print("Forme canonique = " + str(a) + "(x+" + str(-alpha) + ")**2-" + str(-beta))
        elif alpha < 0 and beta >= 0:
            print("Forme canonique = " + str(a) + "(x+" + str(-alpha) + ")**2-" + str(-beta))
        else:
            print("Forme canonique = " + str(a) + "(x+" + str(-alpha) + ")**2-" + str(-beta))'''
        #endregion
        #New
        print("Forme canonique = " + str(a) + "(x +" + str(- alpha) + ")**2 +" + str(beta) + " ---> a(x - alpha)**2 + bêta")
        print("Sur un graphique : Alpha = x | Bêta = y |\na = l'évolution (nombre de carreaux en y / nombre de carreaux en x)")
        if a >= 0:
            print("+inf  Alpha -inf")
            print("  - | Bêta | + \n")
        else:
            print("+inf  Alpha -inf")
            print("  + | Bêta | - \n")
        #endregion
        
        #region Delta
        delta = (b**2) - (4*a*c)
        print("Delta = " + str(delta) + " ---> b**2 - 4ac = " + str(b) + "**2 - 4*" + str(a) + "*" + str(c))

        #print((((-beta) / a) **0.5) + alpha)
        #print("")

        if delta < 0:
            #region Old
            '''delta = -delta
            i = (-1)**0.5

            #X1
            x1 = ((-b) + (i*(delta**0.5))) / (2*a)
            print("X1 = " + str(x1))

            #X2
            x2 = ((-b) - (i*(delta**0.5))) / (2*a)
            print("X2 = " + str(x2))

            print("")

            #Forme factorisé
            print("Forme factorisé = " + str(a) + "(x-" + str(x1) + ")(x-" + str(x2) + ")")
            if str(x1)[1] == "-" and str(x2)[1] == "-":
                print("Forme factorisé = " + str(a) + "(x+" + str(-x1)[1:] + "(x+" + str(-x2)[1:])
            elif str(x1)[1] == "0" or str(x1)[1] == "1" or str(x1)[1] == "2" or str(x1)[1] == "3" or str(x1)[1] == "4" or str(x1)[1] == "5" or str(x1)[1] == "6" or str(x1)[1]=="7" or str(j)[1]=="8" or str(j)[1]=="9"and str(p)[1]=="0" or str(p)[1]=="1" or str(p)[1]=="2" or str(p)[1]=="3" or str(p)[1]=="4" or str(p)[1]=="5" or str(p)[1]=="6" or str(p)[1]=="7" or str(p)[1]=="8" or str(p)[1]=="9":
                print("forme factorisé="+str(a)+"(x-"+str(p)[1:]+"(x-"+str(j)[1:])
            elif str(j)[1]=="0" or str(j)[1]=="1" or str(j)[1]=="2" or str(j)[1]=="3" or str(j)[1]=="4" or str(j)[1]=="5" or str(j)[1]=="6" or str(j)[1]=="7" or str(j)[1]=="8" or str(j)[1]=="9" and str(p)[1]=="-":
                print("forme factorisé="+str(a)+"(x-"+str(j)[1:]+"(x+"+str(-p)[1:])
            elif str(p)[1]=="0" or str(p)[1]=="1" or str(p)[1]=="2" or str(p)[1]=="3" or str(p)[1]=="4" or str(p)[1]=="5" or str(p)[1]=="6" or str(p)[1]=="7" or str(p)[1]=="8" or str(p)[1]=="9" and str(j)[1]=="-":
                print("forme factorisé="+str(a)+"(x+"+str(-j)[1:]+"(x-"+str(p)[1:])
            
            print("Pas de tableau de signe car solution dans les complexes !")'''
            #endregion
            #New
            print("Il n'y a pas de racine car Delta < 0 !")

        elif delta == 0:
            #region Old
            ''''#Forme factorisé
            if alpha >= 0:
                print("Forme factorisé = " + str(a) + "(x-" + str(alpha) + ")**2")
            elif alpha < 0:
                print("Forme factorisé = " + str(a) + "(x+" + str(-alpha) + ")**2")
            
            #Valeur de X
            if a > 0:
                print("Valeur de X = -inf/" + str(alpha) + "/+inf")
                print("Valeur de la fonction = positif sur R ")
            elif a < 0:
                print("Valeur de X = -inf/" + str(alpha)+ "/+inf")
                print("Valeur de la fonction = négatif sur R ")'''
            #endregion
            #New
            #X1
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            print("X1 = " + str(x1) + " ---> -b + √delta / 2a = -" + str(b) + " + √" + str(delta) + " / 2*" + str(a))

            #Forme factorisé
            print("Forme factorisé = " + str(a) + "(x +" + str(-x1) + ")**2 ---> a(x - x1)**2")

        elif delta > 0:
            #region Old
            '''#X1
            x1 = ((-b) + (i*(delta**0.5))) / (2*a)
            print("X1 = " + str(x1))

            #X2
            x2 = ((-b) - (i*(delta**0.5))) / (2*a)
            print("X2 = " + str(x2))

            #Forme factorisé
            if x1 > 0 and x2 > 0:
                print("forme factorisé="+str(a)+"(x-"+str(o)+")(x-"+str(y)+")")
            elif x1 < 0 and x2 < 0:
                print("forme factorisé="+str(a)+"(x+"+str(-o)+")(x+"+str(-y)+")")
            elif x1 < 0 and x2 > 0:
                print("forme factorisé="+str(a)+"(x+"+str(-o)+")(x-"+str(y)+")")
            else:
                print("forme factorisé="+str(a)+"(x-"+str(o)+")(x+"+str(-y)+")")
            
            if a > 0:
                if o>y:
                    print("valeur de X=-inf/"+str(y)+"/"+str(o)+"/+inf")
                    print("valeur de la fonction=positif/"+str(y)+"/negatif/"+str(o)+"/positif")
                elif y<o:
                    print("valeur de X=-inf/"+str(o)+"/"+str(y)+"/+inf")
                    print("valeur de la fonction=positif/"+str(o)+"/negatif/"+str(y)+"/positif")
            if a<0:
                if o<y:
                    print("valeur de X=-inf/"+str(o)+"/"+str(y)+"/+inf")
                    print("valeur de la fonction=negatif/"+str(o)+"/positif/"+str(y)+"/negatif")
                elif y<o:
                    print("valeur de X=-inf/"+str(y)+"/"+str(o)+"/+inf")
                    print("valeur de la fonction=negatif/"+str(y)+"/positif/"+str(o)+"/negatif")'''
            #endregion
            #New
            #X1
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            print("X1 = " + str(x1) + " ---> -b + √delta / 2a = -" + str(b) + " + √" + str(delta) + " / 2*" + str(a))
            #X2
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print("X2 = " + str(x2) + " ---> -b - √delta / 2a = -" + str(b) + " - √" + str(delta) + " / 2*" + str(a))

            #Forme factorisé
            print("Forme factorisé = " + str(a) + "(x +" + str(-x1) + ")(x +" + str(-x2) + ") ---> a(x - x1)(x - x2)")
        #endregion

        print()

        #region Somme
        somme = -b / a
        print("S (somme des racines) = " + str(somme) + " ---> -b / a = " + str(- b) + " / " + str(a))
        #endregion
         
        #region Produit
        produit = c / a
        print("P (produit des racines) = " + str(produit) + " ---> c / a = " + str(c) + " / " + str(a))
        #endregion

        print("ax**2 + bx + c = 0 ---> x**2 - sx + p = 0\n")

        #region Détails
        if a >= 0:
            print("a > 0 donc la fonction est positif sur R ")
        else:
            print("a < 0 donc la fonction est négatif sur R ")
        #print("Valeur de X = -inf/" + str(alpha)+ "/+inf")
        #print("Variation de la fontion = croissante/" + str(beta) + "/decroissante")
        #endregion

        #region Tableau de signe
        if delta < 0:
            print("+inf   -inf")
            print("     " + signe + "     ")
        elif delta == 0:
            print("+inf 0 -inf")
            print("  " + signe + "  |  " + signe + "  ")
        else:
            if a >= 0:
                print("+inf  x1 x2  -inf")
                print("  +  |  -  |  +  ")
            else:
                print("+inf  x1 x2  -inf")
                print("  -  |  +  |  -  ")
        #endregion

def canonique():
    print("Forme canonique = a(x - alpha)**2 + bêta")
    a = int(input("A : "))
    alpha = int(input("Alpha : "))
    beta = int(input("Bêta : "))
    print("Forme canonique = " + str(a) + "(x +" + str(- alpha) + ")**2 +" + str(beta) + "\n")

    
    #region Forme factorisé
    x1 = alpha - math.sqrt(math.sqrt((beta / a)**2))
    print("X1 = " + str(x1) + " ---> Alpha - √|Bêta / a| = " + str(alpha) + " - √|" + str(beta) + " / " + str(a) + '| ---> "|" = valeur absolu = √(√(x**2))')
    x2 = alpha + math.sqrt(math.sqrt((beta / a)**2))
    print("X2 = " + str(x2) + " ---> Alpha + √|Bêta / a| = " + str(alpha) + " + √|" + str(beta) + " / " + str(a) + '| ---> "|" = valeur absolu = √(√(x**2))')

    if x1 == x2:
        print("X1 = X2 donc il y a qu'une seule racine !")
        print("Forme factorisé = " + str(a) + "(x +" + str(-x1) + ")**2 ---> a(x - x1)**2\n")
    else:
        print("Forme factorisé = " + str(a) + "(x +" + str(-x1) + ")(x +" + str(-x2) + ") ---> a(x - x1)(x - x2)\n")
    #endregion

    #region Forme développé
    b = a * ((-alpha) * 2) 
    print("b = " + str(b) + " ---> a * ((-Alpha) * 2) = " + str(a) + " * ((" + str(- alpha) + " * 2)")
    c = alpha**2 * a + beta
    print("c = " + str(c) + " ---> Alpha**2 * a + Bêta = " + str(alpha) + "**2 * " + str(a) + " + " + str(beta)) 
    print("Forme développé = " + str(a) + "x**2 +" + str(b) + "x +" + str(c) + " ---> pour justifier il faut développé\n")
    #endregion

    print("Veux-tu maintenant utiliser la forme\ndévelopper pour plus de détails ?")
    print("1 - Oui")
    print("2 - Non")
    continuerFormeDéveloppé = str(input("Choix : "))
    if continuerFormeDéveloppé == "1":
        print()
        développé()

def factorisé():
    print("Combien y'a t-il de racines ?")
    racine = int(input("1 ou 2 racines : "))
    print()

    if racine == 1:
        print("Forme factorsié = a(x - x1)**2")
        a = int(input("A : "))
        x1 = int(input("x1 : "))
        print("Forme factorisé = " + str(a) + "(x +" + str(-x1) + ")**2\n")

        #region Forme canonique
        alpha = (x1 + x1) / 2
        print("Alpha = " + str(alpha) + " ---> (x1 + x1) / 2 = (" + str(x1) + " + " + str(x1) + ") / 2")
        beta = a * ((alpha - x1) * (alpha + x1))
        print("Bêta = " + str(beta) + " ---> a * -((alpha - x1) * (alpha - x1)) = " + str(a) + " * -((" + str(alpha) + " * " + str(x1) + ") * (" + str(alpha) + " * " + str(x1) + "))") 
        print("Forme canonique = " + str(a) + "(x +" + str(- alpha) + ")**2 +" + str(beta) + " ---> a(x - alpha)**2 + bêta\n")
        #endregion
        
        #region Forme développé
        b = a * -(x1 + x1) 
        print("b = " + str(b) + " ---> a * -(x1 + x1) = " + str(a) + " * -(" + str(x1) + " + " + str(x1) + ")")
        c = a * (x1 * x1)
        print("c = " + str(c) + " ---> a * (x1 * x1) = " + str(a) + " * (" + str(x1) + " * " + str(x1) + ")") 
        print("Forme développé = " + str(a) + "x**2 +" + str(b) + "x +" + str(c) + " ---> pour justifier il faut développé\n")
        #endregion

    elif racine == 2:
        print("Forme factorsié = a(x - x1)(x - x2)")
        a = int(input("A : "))
        x1 = int(input("x1 : "))
        x2 = int(input("x2 : "))
        print("Forme factorisé = " + str(a) + "(x +" + str(- x1) + ")(x +" + str(- x2) + ")\n")

        #region Forme canonique
        alpha = (x1 + x2) / 2
        print("Alpha = " + str(alpha) + " ---> (x1 + x2) / 2 = (" + str(x1) + " + " + str(x2) + ") / 2")
        beta = a * ((alpha - x1) * (alpha - x2))
        print("Bêta = " + str(beta) + " ---> a * ((alpha - x1) * (alpha - x2)) = " + str(a) + " * ((" + str(alpha) + " * " + str(x1) + ") * (" + str(alpha) + " * " + str(x2) + "))") 
        print("Forme canonique = " + str(a) + "(x +" + str(- alpha) + ")**2 +" + str(beta) + " ---> a(x - alpha)**2 + bêta\n")
        #endregion

        #region Forme développé
        b = a * -(x1 + x2) 
        print("b = " + str(b) + " ---> a * -(x1 + x2) = " + str(a) + " * -(" + str(x1) + " + " + str(x2) + ")")
        c = a * (x1 * x2)
        print("c = " + str(c) + " ---> a * (x1 * x2) = " + str(a) + " * (" + str(x1) + " * " + str(x2) + ")") 
        print("Forme développé = " + str(a) + "x**2 +" + str(b) + "x +" + str(c) + " ---> pour justifier il faut développé\n")
        #endregion

    else:
        print("Nombre inconnu !\n")

    print("Veux-tu maintenant utiliser la forme\ndévelopper pour plus de détails ?")
    print("1 - Oui")
    print("2 - Non")
    continuerFormeDéveloppé = str(input("Choix : "))
    if continuerFormeDéveloppé == "1":
        print()
        développé()


#region Boucle
activer = True
while activer == True:
    #Choix du programme
    print("============================================")
    print("Quelle forme veux-tu utiliser ?")          
    print("1 - Développé")
    print("2 - Canonique")
    print("3 - Factorisé")
    choix = str(input("Choix : "))
    print()

    #Lance le programme
    if choix == "1":
        développé()
    elif choix == "2":
        canonique()
    elif choix == "3":
        factorisé()
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