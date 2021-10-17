def trouver(a,b,c):
  alpha = -b/(a*2)
  print("Alpha :", alpha)
  
  beta = a*alpha**2 + b*alpha + c
  print("Bêta :", beta)
  
  print("Résultat : " + str(a) + "(x" + str(- alpha) + ")" + str(beta)) 
  
a = int(input("A : "))
b = int(input("B : "))
c = int(input("C : "))
trouver(a, b, c)