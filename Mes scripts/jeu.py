from random import randint
#definition des fonction
def sauvegarde():
    save_w = open('sauvegarde.txt','w')
    save_w.write(moi.name.replace('\n','') + '\n'+ str(moi.cred) + '\n' + str(moi.xp) + '\n' + str(moi.level) + '\n' +str(moi.vie) + '\n' + str(moi.vie_max) + '\n' + moi.arme.replace('\n','') + '\n' + str(moi.arme_p))
    save_w.close()
def renit():
    save_w = open('sauvegarde.txt','w')
    save_w.close()
    save_w = open('inventaire.txt','w')
    save_w.close()

renit()
#definitions des classes
class Personage:
    def __init__(self,nom,vie,vie_max,cred,xp,level,arme,arme_p):

        self.name = nom
        self.vie = vie
        self.vie_max = vie_max
        self.cred = cred
        self.xp = xp
        self.level = level
        self.arme = arme
        self.arme_p = arme_p

    def attaque(self,cible):

        cible.vie = cible.vie - self.arme_p
        if (cible.vie <= 0):
            cible.vie = 0
            return 1
        else:
            return 0
    def recu_vie(self,vie):
        vie_rest = self.vie + vie
        if (vie_rest > self.vie_max):
            self.vie = self.vie_max
        else:
            self.vie = vie_rest
    def perd_credit(self,cred):
        cred_rest = self.cred - cred
        if(cred_rest >= 0):
            self.cred = cred_rest
            return 1
        else:
            return 0
    def gain_credit (self,cred):
        self.cred = self.cred +cred
        
    def gain_xp(self,xp):
        xp = self.xp + int(xp)
        xp_pour_level =int(( self.level / 10 )* 17587)
        if(xp >= xp_pour_level):
            self.xp = int(xp) - xp_pour_level
            self.level = self.level + 1
            self.vie_max = self.vie_max + 150
            self.vie = self.vie_max
        else:
            self.xp = int(xp)
    def change_arme (self,arme,arme_p):
        self.arme = arme
        self.arme_p = arme_p    
    
class Adverssaire:
    def __init__(self,nom,vie,vie_max,level,arme):

        self.name = nom
        self.vie = vie
        self.vie_max = vie_max
        self.level = level
        self.arme = arme
        
    def attaque(self,cible):
        x = int(cible.arme_p)
        y = int(cible.arme_p/7)
        z = randint(y,x)
        cible.vie = cible.vie - z
        if (cible.vie <= 0):
            cible.vie = 0
            return 1
        else:
            return 0  
# verif fichier de sauvegarde
save_r = open('sauvegarde.txt', 'r')
save = save_r.read()
save_r.close()
if (save == ""):
    #demande du nom du joueur
    name = input("Saisissez votre prénom \n")
    rep = input("vous êtes sur(y ou n) \n")
    #on demande au joueur de vérifier son nom
    while(rep != '0'):
        if(rep == 'y'):
            rep='0'
        elif(rep == 'n'):
            name = input("Saisissez votre prénom \n")
            rep='0'
        else:
            rep='0'
    print("donc vous vous appeler ",name," et pour commencer vous disposé de 0xp et 1000 credits, votre niveau est 1")
    save_w = open('sauvegarde.txt','w')
    save_w.write(name + '\n1000 \n0\n1\n100\n100\népée de débutant\n15')
    save_w.close()
    save_inv = open('inventaire.txt','w')
    save_inv.write('épée de débutant\narme\n15\n1\n')
    save_inv.close()
    
else:
    save = 0
    
#importation des données
    
save_r = open('sauvegarde.txt', 'r')

name = save_r.readline().replace('/n','')
cred = int( save_r.readline())
xp = int(save_r.readline())
level = int(save_r.readline())
vie = int(save_r.readline())
vie_max = int(save_r.readline())
arme = save_r.readline().replace('/n','')
arme_p = int(save_r.readline())
save_r.close()
moi= Personage(name,vie,vie_max,cred,xp,level,arme,arme_p)

#début du jeu
game_over = 0
fin = 0 #mise en place de la variable qui mettra fin au jeu
if(save == 0):
    print("bonjour " + moi.name)
while( fin == 0):
    rep = input("vous pouvez accéder à toutes les commandes du jeux avec la commande /info commande \n")
    
    if(rep == "/info commande"):
        print("/fin : mets fin au jeu\n/combat : lance un combat aléatoirement\n/shop : acheter des armes\n/invent te permet d'acceder à ton inventaire\n/renit : réinitialiser la session")
        
    elif(rep == "/fin"):
        fin = 1
        
    elif(rep == "/shop"):
        shop = open('shop.txt', 'r')
        x=1
        i=1
        while(x==1):
            num = shop.readline().replace('\n','')
            name_o = shop.readline().replace('\n','')
            cred = shop.readline().replace('\n','')
            if(num == ""):
                x=0
                shop.close()
            else:
                print(num + ")------------------------------------------------")
                print(name_o +' ' + cred + ' crédits')
                tp = shop.readline().replace('\n','')
                if(tp == "arme"):
                    armeop = shop.readline().replace('\n','')
                    print("Force "+ armeop)
                elif(tp == "nour"):
                    armeop = shop.readline().replace('\n','')
                    print("vie rendu "+ armeop)
        print('\nVous avez ' + str(moi.cred) +' crédits\n')
        rep_shop = input("écrivez le numéro de l'article: ")
        x=1
        shop = open('shop.txt','r')
        while(x==1):
            num = shop.readline().replace('\n','')
            
            if(num == ""):
                x=0
                shop.close()
            else:   
                name_o = shop.readline().replace('\n','')
                cred = int(shop.readline().replace('\n',''))
                typ = shop.readline().replace('\n','')
                op = int(shop.readline().replace('\n',''))
                
                if(num == str(rep_shop)):
                    rep_shop_achat = input('Voulez vous achetez ' + name_o + ' ? ')
                    if(typ == 'nour'):
                        if(rep_shop_achat == 'y'):
                            rep_cb_ob = input("combien en voulez vous ? ")
                            cred = (int(cred) * int(rep_cb_ob))
                            resu = moi.perd_credit(cred)
                            if(resu == 1):
                                moi.gain_xp(int(cred)/3)
                                
                                sauvegarde()
                            
                                i=0
                                z=0
                                li = []
                                f = open("inventaire.txt","r")
                                while(i==0):
                                    ligne = f.readline()
                                    if name_o in ligne :
                                        a = f.readline()
                                        b = f.readline()
                                        c = f.readline().replace('\n','')
                                        c=(int(c)+int(rep_cb_ob))
                                        li.append(ligne)
                                        li.append(a)
                                        li.append(b)
                                        ligne = c
                                        z=1
                                    elif(ligne == ''):
                                        i=1
                                    li.append(ligne)
                                g = open('inventaire.txt','w')
                                g.close()
                                f.close()
                                h = open('inventaire.txt','a')
                                p = len(li)
                                y=0

                                while(y<p):
                                    ligne = li[y]
                                    h.write(str(ligne))
                                    y=y+1
                                if(z==0):
                                    h.write(name_o+'\n')
                                    h.write(typ+'\n')
                                    h.write(str(op)+'\n')
                                    h.write(str(rep_cb_ob)+'\n')
                                h.close()
                                    
                                sauvegarde()
                            else:
                                print("vous n'avez pas assez de crédits")
                    else:
                        if(rep_shop_achat == 'y'):
                            if(moi.perd_credit(cred)):
                                moi.gain_xp(int(cred)/3)
                                    
                                sauvegarde()
                                    
                                if(typ == "arme"):
                                    moi.arme = name_o
                                    moi.arme_p = op
                                    i=0
                                    z=0
                                    li = []
                                    f = open("inventaire.txt","r")
                                    while(i==0):
                                        ligne = f.readline()
                                        if name_o in ligne :
                                            a = f.readline()
                                            b = f.readline()
                                            c = f.readline()
                                            li.append(ligne)
                                            li.append(a)
                                            li.append(b)
                                            ligne = c
                                            z=1
                                        elif(ligne == ''):
                                            i=1
                                        li.append(ligne)
                                    g = open('inventaire.txt','w')
                                    g.close()
                                    f.close()
                                    h = open('inventaire.txt','a')
                                    p = len(li)
                                    y=0

                                    while(y<p):
                                        ligne = li[y]
                                        h.write(str(ligne))
                                        y=y+1
                                    if(z==0):
                                        h.write(name_o+'\n')
                                        h.write(typ+'\n')
                                        h.write(str(op)+'\n')
                                        h.write('1'+'\n')
                                    h.close()
                                        
                                    sauvegarde()
                            else:
                                print("vous n'avez pas assez de crédits")
            
    elif(rep == "/renit"):
        renit()
        quit()
    
    elif(rep == "/info"):
        print('Vous avez ' + str(moi.cred) + ' crédits')
        print('Vous êtes level ' + str(moi.level) + ' et avez ' + str(moi.xp) + ' xp')
        print('Vous avez ' + moi.arme + ' qui fait ' + str(moi.arme_p) + ' de dégats')
        print('vous avez ' + str(moi.vie) + '/' + str(moi.vie_max) + ' points de vie')

    elif(rep == "/combat"):
        x = int(moi.vie_max/2)
        vie_adver = randint(0,x)+x
        adver = Adverssaire('cyclope',vie_adver,vie_adver,moi.level,'poing')
        combat = 1
        while(combat == 1):
            moi.attaque(adver)
            print('adverssaire touché , il lui reste ' + str(adver.vie) + '/' +  str(adver.vie_max) + 'point de vie')
            if(adver.vie == 0):
                combat = 0
            else:
                adver.attaque(moi)
                print('touché , il me reste ' + str(moi.vie) + '/' +  str(moi.vie_max) + 'point de vie')
                if(moi.vie == 0):
                    game_over = 1
                    combat = 0
         
        if(game_over==0):
            cred = randint(int(adver.vie_max),int(adver.vie_max*4))
            xp = randint(int(adver.vie_max/2),int(adver.vie_max*2))
            moi.gain_xp(xp)
            moi.gain_credit(cred)
            print('Vous avez gagné ' + str(cred) + ' crédits et ' + str(xp) + ' xp')
            
            sauvegarde()
                            
        else:
            print('Vous avez perdu .... réinitiatilastion ....')
            renit()
            quit()
    elif(rep =="/invent"):
        invent=open("inventaire.txt",'r')
        x=0
        while(x==0):
            name_o_inv = invent.readline().replace('\n','')
            if (name_o_inv == ''):
                x=1
            else:
                typ_o_inv = invent.readline().replace('\n','')
                op_o_inv = int(invent.readline().replace('\n',''))
                exemp = int(invent.readline().replace('\n',''))
                
                print('-----------------------------------\n' + name_o_inv + ' en ' + str(exemp) + ' fois')
        invent.close()
        rep_invent= input("choisissez votre objet : ")
        y=0
        invent=open("inventaire.txt",'r')
        while(y==0):
            name_o_inv = invent.readline().replace('\n','')
            if (name_o_inv == ''):
                y=1
            elif(name_o_inv == rep_invent):
                typ_o_inv = invent.readline().replace('\n','')
                op_o_inv = int(invent.readline().replace('\n',''))
                exemp = int(invent.readline().replace('\n',''))
                nv = invent.readline().replace('\n','')
                if(typ_o_inv !='arme'):
                    nb_use = input("\nCombien voulez vous en utiliser? ")
                    nb_rest = exemp - int(nb_use)
                    if(nb_rest <0):
                        nb_rest = 0
                        nb_use = exemp
                    vie_rec = (op_o_inv * int(nb_use))
                    moi.recu_vie(vie_rec)
                    sauvegarde()
                    x=0
                    li = []
                    f = open("inventaire.txt","r")
                    while(x==0):
                        ligne = f.readline()
                        if name_o_inv in ligne :
                            a = f.readline()
                            b = f.readline()
                            c = f.readline()
                            if(nb_rest == 0):
                                a=0
                                b=0
                                c=0
                                ligne = f.readline()
                            else:
                                li.append(ligne)
                                li.append(a)
                                li.append(b)
                                li.append(str(nb_rest) +'\n')
                                ligne =''
                        elif(ligne == ''):
                            x=1
                        li.append(ligne)
                    g = open('inventaire.txt','w')
                    g.close()
                    f.close()
                    h = open('inventaire.txt','a')
                    x = len(li)
                    y=0

                    while(y<x):
                        ligne = li[y]
                        h.write(ligne)
                        y=y+1
                    h.close()
                else:
                    moi.change_arme(name_o_inv,op_o_inv)
                    sauvegarde()
                    
        invent.close()
    else:
        print("mauvaise commande!\n")
quit()