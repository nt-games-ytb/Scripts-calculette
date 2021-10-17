from kandinsky import *

def test1():
  pixel_x = 0
  pixel_y = 0
  rouge = 0
  vert = 0
  bleu = 0
  activer = True
  while activer == True:
    set_pixel(pixel_x,pixel_y,color(rouge,vert,bleu))
  
    #Changement de ligne
    if pixel_x == 320:
      pixel_x = 0
      pixel_y = pixel_y + 1
      rouge = 0
      vert = 0
      bleu = 0
    else:
      pixel_x = pixel_x + 1
      
    #Couleur
    if rouge < 254:
      rouge = rouge + 1
    elif rouge == 255:
      print("test")
      
    #nt games (à finir)
    if pixel_y == 222:
      set_pixel(100,100,color(255,255,255))