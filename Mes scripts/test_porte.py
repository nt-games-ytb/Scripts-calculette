from math import *
from kandinsky import *
from time import *
from random import *

def veg(x,y,c):
  for i in range(int(200*pi)):
    if c:
      f=cos(4*pi*(i/100))+sin(3*pi*(i/100))
    else:
      f=cos(4*pi*(i/100))+sin(3*(i/100))
    set_pixel(int(x+f*cos(i/100)*7),int(y+f*sin(i/100)*7),(0,50,0))
    
def cir(x,y,r,c,col1=0):
  if c==1:
    col1=(255,0,0)
    col2=(255,120,0)
  elif c==0:
    col1=(255,120,0)
    col2=(255,0,0)
  for i in range(x-r,x+r+1):
    for k in range(y-r,y+r+1):
      if sqrt((i-x)**2+(k-y)**2)<r:
        set_pixel(i,k,col1)
  if c<2:
    fill_rect(x-r,y-2,r*2+1,4,col2)


fill_rect(0,0,44,222,(60,60,60))
fill_rect(44,0,20,222,(100,100,100))
fill_rect(64,0,192,222,(88,41,0))
fill_rect(256,0,20,222,(100,100,100))
fill_rect(276,0,44,222,(60,60,60))
fill_rect(168,16,72,78,(255,255,0))
fill_rect(80,110,72,78,(255,255,0))
cir(231,211,9,2,(150,150,150))
fill_rect(223,211,17,11,(150,150,150))
fill_rect(197,215,34,7,(115,115,115))
cir(197,220,5,2,(115,115,115))