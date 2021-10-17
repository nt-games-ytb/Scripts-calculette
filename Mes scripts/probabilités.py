#Introduction
print("Bonjour. Bienvenue dans probabilités.py créer par nt games !")
print("Ce programme est encore en développement !")
print("")

activer = True
while activer == True:

  #Choix
  print("Choisis ce que tu veux calculer :")

  print("1 - P(A)")
  print("2 - P(A) barre")
  print("3 - Pb(A)")
  print("4 - P(A Union B)")
  print("5 - P(A Inter B)")

  choix = str(input("Choix : "))
  print("")

  #Séléctionne des formules

  #P(A)
  if choix == "1":
    print("P(A) = P(A Inter B) + P(A Inter B barre)")
    print("P(A) = P(A Inter B) / P(B)")

  #P(A) barre
  if choix == "2":
      print("P(A) barre = 1 - P(A)")

  #Pb(A)
  if choix == "1":
      print("P(A) = P(A Inter B) + P(A Inter B barre)")
      print("P(A) = P(A Inter B) / P(B)")

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