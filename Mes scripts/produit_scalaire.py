Théorème de pythagore :
Le triangle BAC est rectangle en A
donc : BC**2 = BA**2 + CA**2

Théorème d'Al Kashi :
Dans un triangle ABC, on a, avecles notations de la figure :
a**2 = b**2 + c**2 - 2bc * cos(A)

Identité remarquable :
    ->   ->       ->        -> ->   ->
1. (AB - AC)**2 = AB**2 - 2*AB*AC + AC**2  
    ->   ->  ->   ->    ->      ->
2. (AB + AC)(AB - AC) = AB**2 - AC**2

Etape 1 : Calculer les vecteurs
->   (xB - xA)   (xAB)  
AB = (yB - yA) = (yAB)
#           ->    ->
#à savoir : BA = -AB
Puis :
  ->
||AB|| = √(x**2 + y**2)



#Etape 3 : Calculer les angles
#Soit un triangle équilatéral ABC de côté a
Definition 1 : [si on connait ou on veut connaitre un angle]
->   ->     ->       ->
AB * AC = ||AB|| * ||AC|| * cos(BAC)
                    ->   ->       ->       ->
Donc : BAC = arcos((AB * AC) / (||AB|| * ||AC||))

===============================================================

Définition 2 : [si on connait les longueurs de tout les côtés]
->   ->         ->   ->          ->          ->
AB * AC = 1/2(||AB + AC||**2 - ||AB||**2 - ||AC||**2)
= 1/2(AB**2 + AC**2 - BC**2)

===============================================================

Définition 3 : [si c'est un projeté orthogonal]
- Si on a deux vecteurs qui forment un angle droit alors il sont nul (= 0)
- Le projeté orthogonal est le point d'intersection H qui passe
par la droite d perpendiculaire avec le point M
->   ->   ->   ->  
OA * OB = OA * OH (voir Ivan Monka)

===============================================================

#Etape 2 : Déterminer les produits scalaire
Définition 4 : [si c'est un repére orthonormé]
->   ->
AB * AC = xAB * xAC + yAB * yAC