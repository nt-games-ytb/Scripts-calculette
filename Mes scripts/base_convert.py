#Introduction
print("Bonjour. Bienvenue dans base_convert.py créer par nt games !")
print("")

activer = True
while activer == True:
    #Choix
    print("Choisis ce que tu veux convertir :")

    print("1 - Base 10 en binaire")
    print("2 - Binaire en base 10")
    print("3 - Base 10 en hexadécimal")
    print("4 - Hexadécimal en base 10")
    print("5 - N'importe quelle base en base 10")

    choix = str(input("Choix : "))
    print("")

    #Base 10 en binaire
    if choix == "1":
        nombre = int(input("Nombre : "))
        print(bin(nombre)[2:])
        print("")

    #Binaire en base 10
    if choix == "2":
        binaire = input("Binaire : ")
        print(int(binaire, 2))
        print("")

    #Base 10 en hexadécimal
    if choix == "3":
        nombre = int(input("Nombre : "))
        print(hex(nombre)[2:])
        print("")

    #Hexadécimal en base 10
    if choix == "4":
        hexadecimal = input("Hexadecimal : ")
        print(int(hexadecimal, 16))
        print("")

    #N'importe quelle base en base 10
    if choix == "5":
        base = int(input("Base : "))
        nombre = input("Nombre : ")
        print(int(nombre, base))
        print("")