activer=True
while activer==True:
    num1 = int(input("Numéro du premier terme : "))
    nombre1 = int(input("Nombre du premier terme : "))
    num2 = int(input("Numéro du deuxième terme : "))
    nombre2 = int(input("Nombre du deuxième terme : "))
    raison = (nombre2 - nombre1) / (num2 - num1)
    premier_terme = nombre1 - (raison * num1)
    print("\nRaison : " + str(raison))
    print("Prtemier terme : " + str(premier_terme) + "\n")