print("Bonjour. Bienvenue dans base_convert.py créer par nt games !\n")
activer = True
while activer == True:
    print("Choisis ce que tu veux convertir :")
    print("1 - Base 10 en binaire")
    print("2 - Binaire en base 10")
    print("3 - Base 10 en hexadécimal")
    print("4 - Hexadécimal en base 10")
    print("5 - N'importe quelle base en base 10")
    choix = str(input("Choix : "))
    print()
    if choix == "1":
        nombre = int(input("Nombre : "))
        print(bin(nombre)[2:])
    elif choix == "2":
        binaire = input("Binaire : ")
        print(int(binaire, 2))
    elif choix == "3":
        nombre = int(input("Nombre : "))
        print(hex(nombre)[2:])
    elif choix == "4":
        hexadecimal = input("Hexadecimal : ")
        print(int(hexadecimal, 16))
    elif choix == "5":
        base = int(input("Base : "))
        nombre = input("Nombre : ")
        print(int(nombre, base))
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