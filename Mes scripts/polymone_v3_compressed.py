import math
def développé():
    print("Forme développé = ax**2 + bx + c")
    a = int(input("A : "))
    b = int(input("B : "))
    c = int(input("C : "))
    if a == 0:
        print("Ce n'est pas un polnyônme du 2nd degré !\nTu peux la résoudre de tête !")
    else:
        print("Forme développé = " + str(a) + "x**2 +" + str(b) + "x +" + str(c) + "\n")
        signe = ""
        if a >= 0:
            signe = "+"
        else:
            signe = "-"
        alpha = (-b) / (2*a)
        print("Alpha = " + str(alpha)  + " ---> -b / 2a = -" + str(b) + " / 2*" + str(a))
        beta = -((b**2) - (4*a*c)) / (4*a)
        print("Bêta = " + str(beta) + " ---> - (b**2 - 4ac) / 4a = - (" + str(b) + "**2 - 4*" + str(a) + "*" + str(c) + ") / 4*" + str(a) + " aussi égal à : a * alpha**2 + b * alpha + c")
        print("Forme canonique = " + str(a) + "(x +" + str(- alpha) + ")**2 +" + str(beta) + " ---> a(x - alpha)**2 + bêta")
        print("Sur un graphique : Alpha = x | Bêta = y |\na = l'évolution (nombre de carreaux en y / nombre de carreaux en x)")
        if a >= 0:
            print("+inf  Alpha -inf")
            print("  - | Bêta | + \n")
        else:
            print("+inf  Alpha -inf")
            print("  + | Bêta | - \n")
        delta = (b**2) - (4*a*c)
        print("Delta = " + str(delta) + " ---> b**2 - 4ac = " + str(b) + "**2 - 4*" + str(a) + "*" + str(c))
        if delta < 0:
            print("Il n'y a pas de racine car Delta < 0 !")
        elif delta == 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            print("X1 = " + str(x1) + " ---> -b + √delta / 2a = -" + str(b) + " + √" + str(delta) + " / 2*" + str(a))
            print("Forme factorisé = " + str(a) + "(x +" + str(-x1) + ")**2 ---> a(x - x1)**2")
        elif delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            print("X1 = " + str(x1) + " ---> -b + √delta / 2a = -" + str(b) + " + √" + str(delta) + " / 2*" + str(a))
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print("X2 = " + str(x2) + " ---> -b - √delta / 2a = -" + str(b) + " - √" + str(delta) + " / 2*" + str(a))
            print("Forme factorisé = " + str(a) + "(x +" + str(-x1) + ")(x +" + str(-x2) + ") ---> a(x - x1)(x - x2)")
        print()
        somme = -b / a
        print("S (somme des racines) = " + str(somme) + " ---> -b / a = " + str(- b) + " / " + str(a))
        produit = c / a
        print("P (produit des racines) = " + str(produit) + " ---> c / a = " + str(c) + " / " + str(a))
        print("ax**2 + bx + c = 0 ---> x**2 - sx + p = 0\n")
        if a >= 0:
            print("a > 0 donc la fonction est positif sur R ")
        else:
            print("a < 0 donc la fonction est négatif sur R ")
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
def canonique():
    print("Forme canonique = a(x - alpha)**2 + bêta")
    a = int(input("A : "))
    alpha = int(input("Alpha : "))
    beta = int(input("Bêta : "))
    print("Forme canonique = " + str(a) + "(x +" + str(- alpha) + ")**2 +" + str(beta) + "\n")
    x1 = alpha - math.sqrt(math.sqrt((beta / a)**2))
    print("X1 = " + str(x1) + " ---> Alpha - √|Bêta / a| = " + str(alpha) + " - √|" + str(beta) + " / " + str(a) + '| ---> "|" = valeur absolu = √(√(x**2))')
    x2 = alpha + math.sqrt(math.sqrt((beta / a)**2))
    print("X2 = " + str(x2) + " ---> Alpha + √|Bêta / a| = " + str(alpha) + " + √|" + str(beta) + " / " + str(a) + '| ---> "|" = valeur absolu = √(√(x**2))')
    if x1 == x2:
        print("X1 = X2 donc il y a qu'une seule racine !")
        print("Forme factorisé = " + str(a) + "(x +" + str(-x1) + ")**2 ---> a(x - x1)**2\n")
    else:
        print("Forme factorisé = " + str(a) + "(x +" + str(-x1) + ")(x +" + str(-x2) + ") ---> a(x - x1)(x - x2)\n")
    b = a * ((-alpha) * 2) 
    print("b = " + str(b) + " ---> a * ((-Alpha) * 2) = " + str(a) + " * ((" + str(- alpha) + " * 2)")
    c = alpha**2 * a + beta
    print("c = " + str(c) + " ---> Alpha**2 * a + Bêta = " + str(alpha) + "**2 * " + str(a) + " + " + str(beta)) 
    print("Forme développé = " + str(a) + "x**2 +" + str(b) + "x +" + str(c) + " ---> pour justifier il faut développé\n")
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
        alpha = (x1 + x1) / 2
        print("Alpha = " + str(alpha) + " ---> (x1 + x1) / 2 = (" + str(x1) + " + " + str(x1) + ") / 2")
        beta = a * ((alpha - x1) * (alpha + x1))
        print("Bêta = " + str(beta) + " ---> a * -((alpha - x1) * (alpha - x1)) = " + str(a) + " * -((" + str(alpha) + " * " + str(x1) + ") * (" + str(alpha) + " * " + str(x1) + "))") 
        print("Forme canonique = " + str(a) + "(x +" + str(- alpha) + ")**2 +" + str(beta) + " ---> a(x - alpha)**2 + bêta\n")
        b = a * -(x1 + x1) 
        print("b = " + str(b) + " ---> a * -(x1 + x1) = " + str(a) + " * -(" + str(x1) + " + " + str(x1) + ")")
        c = a * (x1 * x1)
        print("c = " + str(c) + " ---> a * (x1 * x1) = " + str(a) + " * (" + str(x1) + " * " + str(x1) + ")") 
        print("Forme développé = " + str(a) + "x**2 +" + str(b) + "x +" + str(c) + " ---> pour justifier il faut développé\n")
    elif racine == 2:
        print("Forme factorsié = a(x - x1)(x - x2)")
        a = int(input("A : "))
        x1 = int(input("x1 : "))
        x2 = int(input("x2 : "))
        print("Forme factorisé = " + str(a) + "(x +" + str(- x1) + ")(x +" + str(- x2) + ")\n")
        alpha = (x1 + x2) / 2
        print("Alpha = " + str(alpha) + " ---> (x1 + x2) / 2 = (" + str(x1) + " + " + str(x2) + ") / 2")
        beta = a * ((alpha - x1) * (alpha - x2))
        print("Bêta = " + str(beta) + " ---> a * ((alpha - x1) * (alpha - x2)) = " + str(a) + " * ((" + str(alpha) + " * " + str(x1) + ") * (" + str(alpha) + " * " + str(x2) + "))") 
        print("Forme canonique = " + str(a) + "(x +" + str(- alpha) + ")**2 +" + str(beta) + " ---> a(x - alpha)**2 + bêta\n")
        b = a * -(x1 + x2) 
        print("b = " + str(b) + " ---> a * -(x1 + x2) = " + str(a) + " * -(" + str(x1) + " + " + str(x2) + ")")
        c = a * (x1 * x2)
        print("c = " + str(c) + " ---> a * (x1 * x2) = " + str(a) + " * (" + str(x1) + " * " + str(x2) + ")") 
        print("Forme développé = " + str(a) + "x**2 +" + str(b) + "x +" + str(c) + " ---> pour justifier il faut développé\n")
    else:
        print("Nombre inconnu !\n")
    print("Veux-tu maintenant utiliser la forme\ndévelopper pour plus de détails ?")
    print("1 - Oui")
    print("2 - Non")
    continuerFormeDéveloppé = str(input("Choix : "))
    if continuerFormeDéveloppé == "1":
        print()
        développé()
activer = True
while activer == True:
    print("============================================")
    print("Quelle forme veux-tu utiliser ?")          
    print("1 - Développé")
    print("2 - Canonique")
    print("3 - Factorisé")
    choix = str(input("Choix : "))
    print()
    if choix == "1":
        développé()
    elif choix == "2":
        canonique()
    elif choix == "3":
        factorisé()
    else:
        print("Choix inconnu !")
    print("\nVeux-tu continuer ?")
    print("1 - Oui")
    print("2 - Non")
    continuer = str(input("Choix : "))
    if continuer == "1":
        print()
    else:
        exit()