# Type your text here
def racine(a,b,c):
    if a==0:
        print("c'est pas un polnyônme du 2nd degré batard")
    else:
        print("forme developé="+str(a)+"x**2+"+str(b)+"x+"+str(c))
        alpha=(-b)/(2*a)
        beta=((4*a*c)-(b**2))/(4*a)
        print("Alpha"+"="+str(alpha))
        print("Beta"+"="+str(beta))
        delta=(b**2)-(4*a*c)
        print("Delta="+str(delta))
        print((((-beta)/a)**0.5)+alpha)
        if alpha<0 and beta<0:
            print("forme canonique="+str(a)+"(x+"+str(-alpha)+")**2-"+str(-beta))
        elif alpha>=0 and beta>=0:
            print("forme canonique="+str(a)+"(x-"+str(alpha)+")**2+"+str(beta))
        elif alpha<0 and beta>=0:
            print("forme canonique="+str(a)+"(x+"+str(-alpha)+")**2+"+str(beta))
        else:
            print("forme canonique="+str(a)+"(x-"+str(alpha)+")**2-"+str(-beta))
        if delta<0:
            delta=-delta
            i=(-1)**0.5
            j=((-b)+(i*(delta**0.5)))/(2*a)
            p=((-b)-(i*(delta**0.5)))/(2*a)
            print("X1"+"="+str(j))
            print("X2"+"="+str(p))
            print("forme factorisé="+str(a)+"(x-"+str(j)+")(x-"+str(p)+")")
            if str(j)[1]=="-" and str(p)[1]=="-":
                print("forme factorisé="+str(a)+"(x+"+str(-j)[1:]+"(x+"+str(-p)[1:])
            elif str(j)[1]=="0" or str(j)[1]=="1" or str(j)[1]=="2" or str(j)[1]=="3" or str(j)[1]=="4" or str(j)[1]=="5" or str(j)[1]=="6" or str(j)[1]=="7" or str(j)[1]=="8" or str(j)[1]=="9"and str(p)[1]=="0" or str(p)[1]=="1" or str(p)[1]=="2" or str(p)[1]=="3" or str(p)[1]=="4" or str(p)[1]=="5" or str(p)[1]=="6" or str(p)[1]=="7" or str(p)[1]=="8" or str(p)[1]=="9":
                print("forme factorisé="+str(a)+"(x-"+str(p)[1:]+"(x-"+str(j)[1:])
            elif str(j)[1]=="0" or str(j)[1]=="1" or str(j)[1]=="2" or str(j)[1]=="3" or str(j)[1]=="4" or str(j)[1]=="5" or str(j)[1]=="6" or str(j)[1]=="7" or str(j)[1]=="8" or str(j)[1]=="9" and str(p)[1]=="-":
                print("forme factorisé="+str(a)+"(x-"+str(j)[1:]+"(x+"+str(-p)[1:])
            elif str(p)[1]=="0" or str(p)[1]=="1" or str(p)[1]=="2" or str(p)[1]=="3" or str(p)[1]=="4" or str(p)[1]=="5" or str(p)[1]=="6" or str(p)[1]=="7" or str(p)[1]=="8" or str(p)[1]=="9" and str(j)[1]=="-":
                print("forme factorisé="+str(a)+"(x+"+str(-j)[1:]+"(x-"+str(p)[1:])
            print("pas de tableau de signe car solution dans les complexe")
        elif delta==0:
            x=alpha
            print("X"+"="+str(x))
            if x>=0:
                print("forme factorisé="+str(a)+"(x-"+str(x)+")**2")
            elif x<0:
                print("forme factorisé="+str(a)+"(x+"+str(-x)+")**2")
            if a>0:
                print("valeur de X=-inf/"+str(alpha)+"/+inf")
                print("valeur de la fonction=positif sur R ")
            elif a<0:
                print("valeur de X=-inf/"+str(alpha)+"/+inf")
                print("valeur de la fonction=negatif sur R ")
        elif delta>0:
            o=((-b)+(delta**0.5))/(2*a)
            y=((-b)-(delta**0.5))/(2*a)
            print("X1"+"="+str(o))
            print("X2"+"="+str(y))
            if o>0 and y>0:
                print("forme factorisé="+str(a)+"(x-"+str(o)+")(x-"+str(y)+")")
            elif o<0 and y<0:
                print("forme factorisé="+str(a)+"(x+"+str(-o)+")(x+"+str(-y)+")")
            elif o<0 and y>0:
                print("forme factorisé="+str(a)+"(x+"+str(-o)+")(x-"+str(y)+")")
            else:
                print("forme factorisé="+str(a)+"(x-"+str(o)+")(x+"+str(-y)+")")
            if a>0:
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
                    print("valeur de la fonction=negatif/"+str(y)+"/positif/"+str(o)+"/negatif")
        print("")
        if a>0:
            print("valeur de X=-inf/"+str(alpha)+"/+inf")
            print("variation de la fontion=decroissante/"+str(beta)+"/croissante")
        elif a<0:
            print("valeur de X=-inf/"+str(alpha)+"/+inf")
            print("variation de la fontion=croissante/"+str(beta)+"/decroissante")