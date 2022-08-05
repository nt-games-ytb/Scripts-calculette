#Révision de physique-chimie : mouvement et force
activer = True
while activer == True:

  #Choix
  print("Quelle partie veux-tu savoir ?")

  print("1. Système étudiée et référenciel choisit")
  print("2. Direction et sens")
  print("3. Mouvement")
  print("4. Méthode du point d'après (Exemple avec 2)")
  print("5. Méthode centré (Exemple avec 2)")
  print("6. Vecteur variation")
  print("7. Les forces")
  print("8. Relation approchée de la 2ème lois de Newton")

  choix = str(input("Choix : "))
  print("")

  if choix == "1":
    print("- Le système étudiée est la chose au quelle on s'intéresse (skieur, table, ...).")
    print("")
    print("Référenciel héliocentrique : solide immaginaire ---> centre du soleil")
    print("Référenciel géocentrique : solide immaginaire ---> centre de la Terre")
    print("Référenciel terrestre : solide fixe sur la Terre (arbre, ...).")

  elif choix == "2":
    print("La direction est horizontale (_) ou verticale (|).")
    print("Le sens est vers A, vers le haut, vers le bas...")

  elif choix == "3":
    print("Le mouvement est :")
    print("- Rectiligne car c'est une portion de droite")
    print("- Circulaire car un arc de cercle")
    print("- Elliptique car c'est une ellipse")
    print("- Parabolique car c'est une parabole")
    print("")
    print("- Uniforme car la norme de la ou la distance entre les points ne varie pas")
    print("- Accéléré car la norme de la ou la distance entre les points augmente")
    print("- Ralenti car la norme de la ou la distance entre les points diminue")

  elif choix == "4":
    print("Meilleure méthode pour les tracers rectiligne.")
    print("")
    print("- Mesure M2M3 et les convertir si il le faut")
    print("- Faire ||v2|| = M2M3 / T")
    print("- Faire pareil pour ||v3||")
    print("- Les convertir si il le faut : L(v2)")
    print("- Tracer v2 du point M2 vers M3")
    print("- Faire pareil pour v3")

  elif choix == "5":
    print("Meilleure méthode pour les tracers circulaire.")
    print("")
    print("- Tracer et mesurer M0M2 et M2M4")
    print("- Les convertir si il le faut")
    print("- Faire ||v1|| = M0M2 / 2T")
    print("- Faire pareil pour ||v3||")
    print("- Les convertir si il le faut : L(v1)")
    print("- Tracer v1 en partant de M1 et parallèle à M0M2")
    print("- Pareil pour v3")

  elif choix == "6":
    print("Δv(t) = v(t+Δt) - v(t)")
    print("v(t+Δt) doit être parallèle sur le graphique]")
    print("Marche avec les deux méthodes")

  elif choix == "7":
    print("P : L'action à distance par la Terre sur le système")
    print("--> Poids du système")
    print("P = m x g")
    print("")
    print("Rn : L'action de contact par le support sur le système")
    print("--> Réaction normal du support")
    print("")
    print("F : L'action de contact par le frottement sur le système")
    print("--> Force de frottement")
    print("")
    print("T : L'action de contact par la tension sur le système")
    print("--> Tension")
    print("")
    print("ΣF = P + Rn + F + T")
    print("P + Rn = 0   Ils s'annulent")
    print("")
    print("Interraction gravitationelle :")
    print("G = Ma * Mb / D**2 = 6.67 * 10**11 N/m**2 Kg**-2")

  elif choix == "7":
    print("m * Δv = ΣF * Δt")
    print("---> Δv = Δt / m * ΣF = k * ΣF")
    print("")
    print("Dans tout les cas, si Δv = k * ΣF")
    print("alors Δv à la même direction que ΣF.")
    print("Si k > 0 alors Δv à le même sens que ΣF.")

  else:
    print("Mauvaise commande !")

  print("")
  continuer = str(input("Continuer (0=NON,1=OUI) : "))
  if continuer == "0":
    activer = False
  print("")