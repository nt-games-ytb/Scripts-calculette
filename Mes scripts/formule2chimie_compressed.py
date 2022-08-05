Na = 602000000000000000000000
print("Bonjour. Bienvenue dans formule2chimie.py créer par nt games !\n")
activer = True
while activer == True:
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
  print("13 - Rendement (r) [en %]")
  choix = str(input("Choix : "))
  print("")
  if choix == "1":
    print("De quoi veut-tu calculer la masse molaire ?")
    print("1 - Atome")
    print("2 - Molécule")
    choix2 = str(input("Choix : "))
    print("")
    if choix2 == "1":
      m = float(input("Masse de l'entité : "))
      resultat = m * Na
      print("\n" + str(m) + " * " + str(Na) + " = " + str(resultat) + " g/mol")
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
      print("\n" + str(resultat) + " g/mol")
    else:
      print("Erreur sur le choix de la commande !")
  elif choix == "2":
    print("Avec quoi veut-tu calculer la masse ?")
    print("1 - Quantité de matière")
    print("2 - Masse volumique (pour savoir la masse d'un liquide)")
    print("3 - Concentration en masse (Pour savoir la masse de soluté dans notre solution)")
    choix2 = str(input("Choix : "))
    print("")
    if choix2 == "1":
      n = float(input("Quantité de matière : "))
      M = float(input("Masse de l'entité : "))
      resultat = n * M
      print("\n" + str(n) + " * " + str(M) + " = " + str(resultat) + " g")
    elif choix2 == "2":
      p = float(input("Masse volumique : "))
      V = float(input("Volume : "))
      resultat = p * V
      print("\n" + str(p) + " * " + str(V) + " = " + str(resultat) + " g")
    elif choix2 == "3":
      Cm = float(input("Concentration en masse : "))
      V = float(input("Volume : "))
      resultat = Cm * V
      print("\n" + str(Cm) + " * " + str(V) + " = " + str(resultat) + " g")
    else:
      print("Erreur sur le choix de la commande !")
  elif choix == "3":
    print("Avec quoi veut-tu calculer la quantité de matière ?")
    print("1 - Masse")
    print("2 - Concentration")
    print("3 - Volume d'un gaz")
    print("4 - Nombre d'entité")
    choix2 = str(input("Choix : "))
    print("")
    if choix2 == "1":
      m = float(input("Masse : "))
      M = float(input("Masse de l'entité : "))
      resultat = m / M
      print("\n" + str(m) + " / " + str(M) + " = " + str(resultat) + " mol")
    elif choix2 == "2":
      c = float(input("Concentration : "))
      V = float(input("Volume : "))
      resultat = c * V
      print("\n" + str(c) + " / " + str(V) + " = " + str(resultat) + " mol")
    elif choix2 == "3":
      V = float(input("Volume : "))
      Vm = float(input("Volume molaire : "))
      resultat = V / Vm
      print("\n" + str(V) + " / " + str(Vm) + " = " + str(resultat) + " mol")
    elif choix2 == "4":
      N = float(input("Nombre d'entité : "))
      resultat = N / Na
      print("\n" + str(N) + " / " + str(Na) + " = " + str(resultat) + " mol")
    else:
      print("Erreur sur le choix de la commande !")
  elif choix == "4":
    n = float(input("Quantité de matière : "))
    resultat = n * Na
    print("\n" + str(n) + " * " + str(Na) + " = " + str(resultat))
  elif choix == "5":
    m = float(input("Masse : "))
    V = float(input("Volume : "))
    resultat = m / V
    print("\n" + str(m) + " / " + str(V) + " = " + str(resultat) + " g/mL")
  elif choix == "6":
    print("Avec quoi veut-tu calculer la concentration en quantité de matière ?")
    print("1 - Quantité de matière")
    print("2 - Concentration en masse")
    choix2 = str(input("Choix : "))
    print("")
    if choix2 == "1":
      n = float(input("Quantité de matière : "))
      V = float(input("Volume : "))
      resultat = n / V
      print("\n" + str(n) + " / " + str(V) + " = " + str(resultat) + " mol/L")
    elif choix2 == "2":
      Cm = float(input("Concentration en masse : "))
      M = float(input("Masse molaire : "))
      resultat = Cm / M
      print("\n" + str(Cm) + " / " + str(M) + " = " + str(resultat) + " mol/L")
    else:
      print("Erreur sur le choix de la commande !")
  elif choix == "7":
    print("Avec quoi veut-tu calculer la concentration en masse ?")
    print("1 - Masse")
    print("2 - Concentration en masse")
    choix2 = str(input("Choix : "))
    print("")
    if choix2 == "1":
      m = float(input("Masse : "))
      V = float(input("Volume : "))
      resultat = m / V
      print("\n" + str(m) + " / " + str(V) + " = " + str(resultat) + " g/L")
    elif choix2 == "2":
      c = float(input("Concentration en quantité de matière : "))
      M = float(input("Masse molaire : "))
      resultat = c / M
      print("\n" + str(c) + " / " + str(M) + " = " + str(resultat) + " g/L")
    else:
      print("Erreur sur le choix de la commande !")
  elif choix == "8":
    print("Avec quoi veut-tu calculer le volume ?")
    print("1 - Volume molaire")
    print("2 - Concentration")
    print("3 - Concentration en masse")
    print("4 - Masse volumique")
    choix2 = str(input("Choix : "))
    print("")
    if choix2 == "1":
      n = float(input("Quantité de matière : "))
      Vm = float(input("Volume molaire : "))
      resultat = n * Vm
      print("\n" + str(n) + " / " + str(Vm) + " = " + str(resultat) + " L")
    elif choix2 == "2":
      n = float(input("Quantité de matière : "))
      c = float(input("Concentration : "))
      resultat = n / c
      print("\n" + str(n) + " / " + str(c) + " = " + str(resultat) + " L")
    elif choix2 == "3":
      V = float(input("Volume : "))
      Vm = float(input("Volume molaire : "))
      resultat = V / Vm
      print("")
      print("\n" + str(V) + " / " + str(Vm) + " = " + str(resultat) + " L")
    elif choix2 == "4":
      m = float(input("Masse : "))
      p = float(input("Masse volumique : "))
      resultat = m / p
      print("\n" + str(m) + " / " + str(p) + " = " + str(resultat) + " L")
    else:
      print("Erreur sur le choix de la commande !")
  elif choix == "9":
    V = float(input("Volume : "))
    n = float(input("Quantité de matière : "))
    resultat = V / n
    print("\n" + str(V) + " / " + str(n) + " = " + str(resultat) + " L/mol")
  elif choix == "10":
    v = float(input("Vitesse : "))
    t = float(input("Temps : "))
    resultat = v * t
    print("\n" + str(v) + " * " + str(t) + " = " + str(resultat) + " Km")
  elif choix == "11":
    d = float(input("Distance : "))
    t = float(input("Temps : "))
    resultat = d / t
    print("\n" + str(d) + " / " + str(t) + " = " + str(resultat) + " Km/h")
  elif choix == "12":
    d = float(input("Distance : "))
    v = float(input("Vitesse : "))
    resultat = d / v
    resultat2 = (d / v) * 3600
    print("\n" + str(d) + " / " + str(v) + " = " + str(resultat) + " h")
    print(str(d) + " / " + str(v) + " * 3600 = " + str(resultat2) + " s")
  elif choix == "13":
    obtenue = float(input("Masse obtenue : "))
    espéré = float(input("Masse espéré : "))
    resultat = obtenue / espéré * 100
    print("\n" + str(obtenue) + " / " + str(espéré) + " = " + str(resultat) + " %")
  else:
    print("Erreur sur le choix de la commande !")
  print("")
  print("Veux-tu continuer ?")
  print("1 - Oui")
  print("2 - Non")
  continuer = str(input("Choix : "))
  if continuer == "1":
    print("")
  else:
    exit()