#inéquation by Mael Depallens
def inequation():
    print("")
    a = float(input("Choix de a : "))
    b = float(input("Choix de b : "))
    c = float(input("Choix de c : "))
    print("")
    delta = (b**2)-(4*a*c)
    print("Quelle signe : < ; > ; <= ; >=  ")
    signe = str(input("Choix du signe : "))
    if delta < 0 :
        if signe == (">" or ">=") :
            if a > 0 :
                print("S=]-∞;+∞[ ou  S = |R ")
            elif a < 0 :
                print("S = {∅} ")
        else :
            if a < 0 :
                print("S=]-∞;+∞[ ou  S = |R ")
            elif  a > 0 :
                print("S = {∅} ")

    elif delta == 0 :
        X0 = (-b)/(2*a)
        if signe==">" :
            if a > 0 :
                print("S=]-∞;"+str(X0)+"[U]"+str(X0)+";+∞[ ou  S = |R-{"+str(X0)+"} ")
            elif a < 0 :
                print("S = {∅} ")
        elif signe =="<" :
            if a < 0 :
               print("S=]-∞;"+str(X0)+"[U]"+str(X0)+";+∞[ ou  S = |R-{"+str(X0)+"} ")
            elif  a > 0 :
                print("S = {∅} ")

        elif signe == ">=" :
            if a > 0 :
                print("S=]-∞;"+str(X0)+"]U["+str(X0)+";+∞[ ou  S = |R ")
            elif a < 0 :
                print("S = {"+str(X0)+"} ")

        elif signe =="<=" :
            if a < 0 :
               print("S=]-∞;"+str(X0)+"]U["+str(X0)+";+∞[ ou  S = |R-{"+str(X0)+"} ")
            elif  a > 0 :
                print("S = {"+str(X0)+"} ")

    elif delta > 0 :
        X1 = ((-b)+(delta)**0.5)/(2*a)
        X2 = ((-b)-(delta)**0.5)/(2*a)
        if signe == ">" :
            if a > 0 :
                if X1 < X2 :
                    print("S=]-∞;"+str(X1)+"[U]"+str(X2)+";+∞[  ")
                elif X1 > X2 :
                    print("S=]-∞;"+str(X2)+"[U]"+str(X1)+";+∞[  ")
            elif a < 0 :
                if X1 < X2 :
                    print("S=]"+str(X1)+";"+str(X2)+"[  ")
                elif X1 > X2 :
                    print("S=]"+str(X2)+";"+str(X1)+"[  ")

        elif signe == "<" :
            if a < 0 :
                if X1 < X2 :
                    print("S=]-∞;"+str(X1)+"[U]"+str(X2)+";+∞[  ")
                elif X1 > X2 :
                    print("S=]-∞;"+str(X2)+"[U]"+str(X1)+";+∞[  ")
            elif a > 0 :
                if X1 < X2 :
                    print("S=]"+str(X1)+";"+str(X2)+"[  ")
                elif X1 > X2 :
                    print("S=]"+str(X2)+";"+str(X1)+"[  ")
        elif signe == ">=" :
            if a > 0 :
                if X1 < X2 :
                    print("S=]-∞;"+str(X1)+"]U["+str(X2)+";+∞[  ")
                elif X1 > X2 :
                    print("S=]-∞;"+str(X2)+"]U["+str(X1)+";+∞[  ")
            elif a < 0 :
                if X1 < X2 :
                    print("S=["+str(X1)+";"+str(X2)+"]  ")
                elif X1 > X2 :
                    print("S=["+str(X2)+";"+str(X1)+"]  ")
        elif signe == "<=" :
            if a < 0 :
                if X1 < X2 :
                    print("S=]-∞;"+str(X1)+"]U["+str(X2)+";+∞[  ")
                elif X1 > X2 :
                    print("S=]-∞;"+str(X2)+"]U["+str(X1)+";+∞[  ")
            elif a > 0 :
                if X1 < X2 :
                    print("S=["+str(X1)+";"+str(X2)+"]  ")
                elif X1 > X2 :
                    print("S=["+str(X2)+";"+str(X1)+"]  ")