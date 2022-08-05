###############################################
# Nombre dérivé by nt games and Mael | 1er G3 #
###############################################

def derive2e():
    a = float(input("Choix de a : "))
    b = float(input("Choix de b : "))
    c = float(input("Choix de c : "))
    d = float(input("Antécédent du nb dérivé : "))

    A = str(a)
    B = str(b)
    C = str(c)
    D = str(d)

    nb = (2*a*d)+b

    print("")
    print("")

    print("f("+D+"+h) = "+A+"("+D+"+h)**2+"+B+"("+D+"+h)+"+C)
    print("f("+D+"+h) = "+A+"("+str(d**2)+"+"+str(2*d)+"h"+"+h**2)+"+str(b*d)+"+"+B+"h+"+C)
    print("f("+D+"+h) = "+str((d**2)*a)+"+"+str(2*d*a)+"h"+"+"+A+"h**2+"+str(b*d)+"+"+B+"h+"+C)
    print("f("+D+"+h) = "+str(((d**2*a)+(b*d)+c))+"+"+str((2*d*a)+b)+"h"+"+"+A+"h**2")
    print("")

    print("f("+D+") = "+A+"*"+D+"**2+"+B+"*"+D+"+"+C)
    print("f("+D+") = "+str(a*(d**2))+"+"+str(b*d)+"+"+C)
    print("f("+D+") = "+str(a*(d**2)+b*d+c))
    print("")

    s = str(str(((d**2*a)+(b*d)+c))+"+"+str((2*d*a)+b)+"h"+"+"+A+"h**2")
    p = str(str(a*(d**2)+b*d+c))
    print("t = "+"("+s+"-"+p+")/h")
    print("t = ("+str((2*d*a)+b)+"h"+"+"+A+"h**2)/h")
    print("t = "+str((2*d*a)+b)+"+"+A+"h")
    print("")

    x = a*d*2+b
    print("lim t = "+str((2*d*a)+b))
    print("h→0")
    print("")

    print("f'("+D+") = "+str((2*d*a)+b))
    print("")

    print("On sait que le coefficient directeur est egal au nombre derivé donc :")
    print("")
    print("y = "+str(nb)+"x+b")
    print(str(a*(d**2)+b*d+c)+" = "+str(nb)+"*"+D+"+b")
    print("b = "+str(a*(d**2)+b*d+c)+"-"+str(nb*d))
    print("b = "+str((a*(d**2)+b*d+c)-(nb*d)))
    print("")
    print("y = "+str(nb)+"x+"+str((a*(d**2)+b*d+c)-(nb*d)))
    print("")

def derive3e() :
    a = float(input("Choix de a : "))
    b = float(input("Choix de b : "))
    c = float(input("Choix de c : "))
    d = float(input("Choix de d : "))
    e = float(input("Antecedent du nb dérive : "))

    A = str(a)
    B = str(b)
    C = str(c)
    D = str(d)
    E = str(e)

    nb = (3*a*(e**2))+(2*b*e)+c

    print("")
    print("")

    print("f("+E+"+h) = "+A+"("+E+"+h)**3+"+B+"("+E+"+h)**2+"+C+"("+E+"+h)+"+D)
    print("f("+E+"+h) = "+A+"("+str(e**3)+"+"+str(3*(e**2))+"h+"+str(3*e)+"h**2"+"+**3)+"+B+"("+str(e**2)+"+"+str(2*e)+"h"+"+h**2)+"+C+"("+E+"+h)+"+D)
    print("f("+E+"+h) = "+str(a*(e**3))+"+"+str(a*3*(e**2))+"h+"+str(a*3*e)+"h**2"+A+"h**3+"+str(e**2*b)+"+"+str(2*e*b)+"h"+B+"h**2+"+str(e*c)+"+"+C+"h+"+D)
    print("f("+E+"+h) = "+str((a*(e**3))+(e**2*b)+(e*c)+d)+"+"+str((a*3*(e**2))+(2*e*b)+c)+"h+"+str((a*3*e)+b)+"h**2+"+A+"h**3")
    print("")

    print("f("+E+") = "+A+"*"+E+"**3+"+B+"*"+E+"**2+"+C+"*"+E+"+"+D)
    print("f("+E+") = "+str(a*(e**3))+"+"+str((b*(e**2)))+"+"+str(c*e)+"+"+D)
    print("f("+E+") = "+str((a*(e**3))+(b*(e**2))+(c*e)+d))
    print("")

    print("t = ("+str((a*(e**3))+(e**2*b)+(e*c)+d)+"+"+str((a*3*(e**2))+(2*e*b)+c)+"h+"+str((a*3*e)+b)+"h**2+"+A+"h**3"+"-"+str((a*(e**3))+(b*(e**2))+(c*e)+d)+")/h")
    print("t = ("+str((a*3*(e**2))+(2*e*b)+c)+"h+"+str((a*3*e)+b)+"h**2+"+A+"h**3"+")/h")
    print("t = "+str((a*3*(e**2))+(2*e*b)+c)+"+"+str((a*3*e)+b)+"h+"+A+"h**2")
    print("")

    print("lim t = "+str((a*3*(e**2))+(2*e*b)+c))
    print("h→0")
    print("")

    print("f'("+E+") = "+str((a*3*(e**2))+(2*e*b)+c))
    print("")

    print("On sait que le coefficient directeur est egal au nombre derivé donc :")
    print("")
    print("y = "+str(nb)+"x+b")
    print(str(a*(e**3)+b*(e**2)+c*e+d)+" = "+str(nb)+"*"+E+"+b")
    print("b = "+str(a*(e**3)+b*(e**2)+c*e+d)+"-"+str(nb*e))
    print("b = "+str((a*(e**3)+b*(e**2)+c*e+d)-(nb*e)))
    print("")
    print("y = "+str(nb)+"x+"+str((a*(e**3)+b*(e**2)+c*e+d)-(nb*e)))
    print("")

activer = True
while activer == True:
    choix = int(input("Utilisez-vous un polynome du 2nd ou 3ème degré ? "))
    if choix == 2:
        print("")
        derive2e()
    elif choix == 3:
        print("")
        derive3e()
    else:
        print("Erreur sur la commande !")