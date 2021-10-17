#Nombre d'entités par mol (constante d'avogardo)
Na = 602000000000000000000000#6,02*(10**23)

#Introduction
print("Bonjour. Bienvenue dans formule2chimie.py créer par nt games !")
print("")

activer = True
while activer == True:

  #Choix
  print("Choisis ce que tu veux calculer :")

  print("1 - Masse molaire (M) [en g/mol]")
  print("2 - Masse (m) [en g]")
  print("3 - Quantité de matière (n) [en mol]")
  print("4 - Nombre d'entités (N)")
  print("5 - Masse volumique (p) [en g/mL]")
  print("6 - Concentration en quantité de matière de soluté (c) [en mol/L]")
  print("7 - Concentration en masse (Cm) [en g/L]")
  print("8 - Volume (V) [en L]")
  print("9 - Volume molaire (Vm) [en L/mol]")
  print("10 - Distance (d) [en Km]")
  print("11 - Vitesse (v) [en Km/h]")
  print("12 - Temps (t) [en h]")

  choix = str(input("Choix : "))
  print("")

  #Séléctionne des formules

  #Masse molaire
  if choix == "1":
    
    #Choix 2
    print("De quoi veut-tu calculer la masse molaire ?")
    print("1 - Atome")
    print("2 - Molécule")
    
    choix2 = str(input("Choix : "))
    print("")
    
    #Calcule d'un atome (encore en bêta)
    if choix2 == "1":
      m = float(input("Masse de l'entité : "))
      #m = int(input())
      resultat = m * Na
      print("")
      print(str(resultat) + " g/mol")
    
    #Calcule d'une molécule
    elif choix2 == "2":
      nombre = int(input("Nombre d'atomes : "))
      resultat = 0
      print("")
      for i in range(nombre):
        atome = str(input("L'atome : "))
        if atome == "h":
          a = 1
        if atome == "c":
          a = 12
        if atome == "o":
          a = 16
        if atome == "cl":
          a = 35.5
        if atome == "n":
          a = 14
        n = int(input("Nombre de " + atome + " : "))
        resultat = resultat + n * a
      print("")
      print(str(resultat) + " g/mol")
      
    #Commande invalide
    else:
      print("Erreur sur le choix de la commande !")
      
  #Masse
  elif choix == "2":
    
    #Choix 2
    print("Avec quoi veut-tu calculer la masse ?")
    print("1 - Quantité de matière")
    print("2 - Masse volumique (pour savoir la masse d'un liquide)")
    print("3 - Concentration en masse (Pour savoir la masse de soluté dans notre solution)")
    
    choix2 = str(input("Choix : "))
    print("")
    
    #Quantité de matière
    if choix2 == "1":
      n = float(input("Quantité de matière : "))
      M = float(input("Masse de l'entité : "))
      resultat = n * M
      print("")
      print(str(resultat) + " g")
    
    #Masse volumique
    elif choix2 == "2":
      p = float(input("Masse volumique : "))
      V = float(input("Volume : "))
      resultat = p * V
      print("")
      print(str(resultat) + " g")
      
    #Masse volumique
    elif choix2 == "3":
      Cm = float(input("Concentration en masse : "))
      V = float(input("Volume : "))
      resultat = Cm * V
      print("")
      print(str(resultat) + " g")
      
    #Commande invalide
    else:
      print("Erreur sur le choix de la commande !")

    
  #Quantité de matière
  elif choix == "3":
    
    #Choix 2
    print("Avec quoi veut-tu calculer la quantité de matière ?")
    print("1 - Masse")
    print("2 - Concentration")
    print("3 - Volume d'un gaz")
    print("4 - Nombre d'entité")
    
    choix2 = str(input("Choix : "))
    print("")
    
    #Masse
    if choix2 == "1":
      m = float(input("Masse : "))
      M = float(input("Masse de l'entité : "))
      resultat = m / M
      print("")
      print(str(resultat) + " mol")
    
    #Concentration
    elif choix2 == "2":
      c = float(input("Concentration : "))
      V = float(input("Volume : "))
      resultat = c * V
      print("")
      print(str(resultat) + " mol")
      
    #Volume
    elif choix2 == "3":
      V = float(input("Volume : "))
      Vm = float(input("Volume molaire : "))
      resultat = V / Vm
      print("")
      print(str(resultat) + " mol")
      
    #Nombre d'entités
    elif choix2 == "4":
      N = float(input("Nombre d'entité : "))
      resultat = N / Na
      print("")
      print(str(resultat) + " mol")
      
    #Commande invalide
    else:
      print("Erreur sur le choix de la commande !")
    
  #Nombre d'entités
  elif choix == "4":
    n = float(input("Quantité de matière : "))
    resultat = n * Na
    print("")
    print(str(resultat))
    
  #Masse volumique
  elif choix == "5":
    m = float(input("Masse : "))
    V = float(input("Volume : "))
    resultat = m / V
    print("")
    print(str(resultat) + " g/mL")
    
  #Concentration en quantité de matière
  elif choix == "6":

    #Choix 2
    print("Avec quoi veut-tu calculer la concentration en quantité de matière ?")
    print("1 - Quantité de matière")
    print("2 - Concentration en masse")
    
    choix2 = str(input("Choix : "))
    print("")
    
    #Quantité de matière
    if choix2 == "1":
      n = float(input("Quantité de matière : "))
      V = float(input("Volume : "))
      resultat = n / V
      print("")
      print(str(resultat) + " mol/L")

    #Concentration en masse
    elif choix2 == "2":
      Cm = float(input("Concentration en masse : "))
      M = float(input("Masse molaire : "))
      resultat = Cm / M
      print("")
      print(str(resultat) + " mol/L")
      
    #Commande invalide
    else:
      print("Erreur sur le choix de la commande !")
    
  #Concentration en masse
  elif choix == "7":

    #Choix 2
    print("Avec quoi veut-tu calculer la concentration en masse ?")
    print("1 - Masse")
    print("2 - Concentration en masse")
    
    choix2 = str(input("Choix : "))
    print("")
    
    #Masse
    if choix2 == "1":
      m = float(input("Masse : "))
      V = float(input("Volume : "))
      resultat = m / V
      print("")
      print(str(resultat) + " g/L")

    #Concentration en quantité de matière
    elif choix2 == "2":
      c = float(input("Concentration en quantité de matière : "))
      M = float(input("Masse molaire : "))
      resultat = c / M
      print("")
      print(str(resultat) + " g/L")
      
    #Commande invalide
    else:
      print("Erreur sur le choix de la commande !")
    
  #Volume
  elif choix == "8":

    #Choix 2
    print("Avec quoi veut-tu calculer le volume ?")
    print("1 - Volume molaire")
    print("2 - Concentration")
    print("3 - Concentration en masse")
    print("4 - Masse volumique")
    
    choix2 = str(input("Choix : "))
    print("")
    
    #Volume molaire
    if choix2 == "1":
      n = float(input("Quantité de matière : "))
      Vm = float(input("Volume molaire : "))
      resultat = n * Vm
      print("")
      print(str(resultat) + " L")
    
    #Concentration
    elif choix2 == "2":
      n = float(input("Quantité de matière : "))
      c = float(input("Concentration : "))
      resultat = n / c
      print("")
      print(str(resultat) + " L")
      
    #Concentration en masse
    elif choix2 == "3":
      V = float(input("Volume : "))
      Vm = float(input("Volume molaire : "))
      resultat = V / Vm
      print("")
      print(str(resultat) + " L")
      
    #Masse volumique
    elif choix2 == "4":
      m = float(input("Masse : "))
      p = float(input("Masse volumique : "))
      resultat = m / p
      print("")
      print(str(resultat) + " L")
      
    #Commande invalide
    else:
      print("Erreur sur le choix de la commande !")
    
  #Volume molaire
  elif choix == "9":
    V = float(input("Volume : "))
    n = float(input("Quantité de matière : "))
    resultat = V / n
    print("")
    print(str(resultat) + " L/mol")

  #Distance v = d / t
  elif choix == "10":
    v = float(input("Vitesse : "))
    t = float(input("Temps : "))
    resultat = v * t
    print("")
    print(str(resultat) + " Km")

  #Vitesse
  elif choix == "11":
    d = float(input("Distance : "))
    t = float(input("Temps : "))
    resultat = d / t
    print("")
    print(str(resultat) + " Km/h")

  #Temps
  elif choix == "12":
    d = float(input("Distance : "))
    v = float(input("Vitesse : "))
    resultat = d / v
    resultat2 = (d / v) * 3600
    print("")
    print(str(resultat) + " h")
    print(str(resultat2) + " s")
    
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