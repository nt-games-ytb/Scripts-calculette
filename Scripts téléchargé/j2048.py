from kandinsky import *
from random import *
from time import *
from ion import *

v=[0]*16
chiffres = [31599,18724,29671,31207,18925,31183,31695,18727,31727,31215]
sco = 0

def aff(n,x,y):
  if n>0:
    for k,c in enumerate(str(n)):
      for i in range(16):
        if chiffres[int(c)]>>i & 1 == 1:
          fill_rect(x+12*k+(i%3)*3,y+(i//3)*3,3,3,(110,110,90))
        
def ajout():
  vides = [i for i,x in enumerate(v) if x==0]
  if len(vides) != 0:
    v[choice(vides)] = choice([2,2,2,4])
  plateau()
  
def gauche(r):
  return ([x for x in r if x!=0]+[0]*4)[:4]

def simp(r):
  global sco
  r = gauche(r)
  for i in range(1,4):
    if r[i] == r[i-1]:
      r[i-1] *= 2
      r[i] = 0
      sco += r[i-1]
  return gauche(r)    

def calcul(ligne,pas):
  for i in range(4):
    pos = simp([v[ligne[k]+pas*i] for k in range(4)])
    for k in range(4):
      v[ligne[k]+pas*i] = pos[k]
  ajout()
          
def plateau():
  global sco
  fill_rect(3,6,208,208,(190,170,160))
  for i in range(16):
    g = max(0,int(-v[i]/2+255))
    fill_rect(5+50*(i%4),8+50*(i//4),47,47,(g,g,g))
    aff(v[i],7+50*(i%4)+24-6*len(str(v[i])),25+50*(i//4))
  draw_string(("0000"+str(sco))[-5:],250,10)
    
def go():
  ajout()
  while True:
    if keydown(KEY_LEFT): calcul([0,1,2,3],4)
    elif keydown(KEY_RIGHT): calcul([3,2,1,0],4)
    elif keydown(KEY_UP): calcul([0,4,8,12],1)
    elif keydown(KEY_DOWN): calcul([12,8,4,0],1)
    sleep(.1)
    
go()