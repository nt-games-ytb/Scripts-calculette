########################################################################################
#                                                                                      #
#  ###  ###  #    # #  #   #  ###  #   #  ###   # #  ###                               #
#  # #  # #  #    # #  ##  #  # #  ## ##  #     # #    #                               #
#  ###  # #  #    ###  # # #  # #  # # #  ##    # #  ###                               #
#  #    # #  #     #   #  ##  # #  #   #  #     # #  #                                 #
#  #    ###  ###   #   #   #  ###  #   #  ### #  #   ### by nt games and Mael | 1er G3 #
#                                                                                      #
########################################################################################

#Import
import math

#Fonction
def racine(a,b,c):
    if a == 0:
        print("Ce n'est pas un polnyônme du 2nd degré !")

    else:
        #Forme développé
        print("Forme developé = " + str(a) + "x**2+" + str(b) + "x+" + str(c))
        print("")

        #Alpha
        alpha = (-b) / (2*a)
        print("Alpha = " + str(alpha))

        #Bêta
        beta = ((4*a*c) - (b**2)) / (4*a) #Technique 2
        print("Bêta = " + str(beta))

        #Forme canonique
        #Old
        '''if alpha < 0 and beta < 0:
            print("Forme canonique = " + str(a) + "(x+" + str(-alpha) + ")**2-" + str(-beta))
        elif alpha >= 0 and beta >= 0:
            print("Forme canonique = " + str(a) + "(x+" + str(-alpha) + ")**2-" + str(-beta))
        elif alpha < 0 and beta >= 0:
            print("Forme canonique = " + str(a) + "(x+" + str(-alpha) + ")**2-" + str(-beta))
        else:
            print("Forme canonique = " + str(a) + "(x+" + str(-alpha) + ")**2-" + str(-beta))'''
        #New
        print("Forme canonique : " + str(a) + "(x+" + str(- alpha) + ")**2" + str(beta))
        print("")

        #Delta
        delta = (b**2) - (4*a*c)
        print("Delta = " + str(delta))

        #print((((-beta) / a) **0.5) + alpha)
        #print("")

        if delta < 0:
            #Old
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
            #New
            print("Il n'y a pas de racine car Delta < 0 !")

        elif delta == 0:
            #Old
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
            #New
            #X1
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            print("X1 = " + str(x1))

            #Forme factorisé
            print("Forme factorisé = " + str(a) + "(x+" + str(-x1) + ")**2")

        elif delta > 0:
            #Old
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
            #New
            #X1
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            print("X1 = " + str(x1))
            #X2
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print("X2 = " + str(x2))

            #Forme factorisé
            print("Forme factorisé = " + str(a) + "(x+" + str(-x1) + ")(x+" + str(-x2) + ")")


        print("")

        #Détails
        if a >= 0:
            print("La fonction est positif sur R ")
        else:
            print("La fonction est négatif sur R ")
        #print("Valeur de X = -inf/" + str(alpha)+ "/+inf")
        #print("Variation de la fontion = croissante/" + str(beta) + "/decroissante")

        #Tableau de signe
        #Signe
        signe = ""
        if a >= 0:
            signe = "+"
        else:
            signe = "-"
        #Tableau
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

#Boucle
activer = True
while activer == True:
    #Lance le program
    a = int(input("A : "))
    b = int(input("B : "))
    c = int(input("C : "))
    print("")
    racine(a,b,c)

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