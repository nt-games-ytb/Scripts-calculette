import math
def racine(a,b,c):
    if a == 0:
        print("Ce n'est pas un polnyônme du 2nd degré !")
    else:
        print("Forme developé = " + str(a) + "x**2+" + str(b) + "x+" + str(c))
        print("")
        alpha = (-b) / (2*a)
        print("Alpha = " + str(alpha))
        beta = ((4*a*c) - (b**2)) / (4*a)
        print("Bêta = " + str(beta))
        print("Forme canonique : " + str(a) + "(x+" + str(- alpha) + ")**2" + str(beta))
        print("")
        delta = (b**2) - (4*a*c)
        print("Delta = " + str(delta))
        if delta < 0:
            print("Il n'y a pas de racine car Delta < 0 !")
        elif delta == 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            print("X1 = " + str(x1))
            print("Forme factorisé = " + str(a) + "(x+" + str(-x1) + ")**2")
        elif delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            print("X1 = " + str(x1))
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print("X2 = " + str(x2))
            print("Forme factorisé = " + str(a) + "(x+" + str(-x1) + ")(x+" + str(-x2) + ")")
        print("")
        if a >= 0:
            print("La fonction est positif sur R ")
        else:
            print("La fonction est négatif sur R ")
        signe = ""
        if a >= 0:
            signe = "+"
        else:
            signe = "-"
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
activer = True
while activer == True:
    a = int(input("A : "))
    b = int(input("B : "))
    c = int(input("C : "))
    print("")
    racine(a,b,c)
    print("")
    print("Veux-tu continuer ?")
    print("1 - Oui")
    print("2 - Non")
    continuer = str(input("Choix : "))
    if continuer == "1":
        print("")
    else:
        exit()