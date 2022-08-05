from time import sleep
from kandinsky import *
from math import log
from random import *
from ion import *
def t2048(tab):
  fill_rect(0,0,320,222,(255,255,255))
  for i in range(5):
    fill_rect(i*50+60,22,1,200,(0,0,0))
  for i in range(5):
    fill_rect(60,i*50+22,200,1,(0,0,0))
  for i in range(4):
    for k in range(4):
      x=tab[k][i]
      if x<10:dec=20
      elif x<100:dec=15
      elif x<1000:dec=10
      else:dec=5
      if x>0:
        col=(max(0,255-51*(int(log(x,2))-1)),255,max(0,int(log(x,2)-1)*51-255))
        fill_rect(61+i*50,23+k*50,49,49,col)
        draw_string(str(x),60+i*50+dec,39+k*50,(0,0,0),col)
def chknum(n,tab):
  lst=[]
  for i in range(4):
    for k in range(4):
      if n==tab[i][k]:lst.append([i,k])
  return lst

def p2048():
  score=0
  tab=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  tab[randint(0,3)][randint(0,3)]=2
  canspawn=True
  while True:
    if canspawn or tr:
      new=choice(chknum(0,tab))
      tab[new[0]][new[1]]=2*randint(1,2)
    canmove=0
    act=[0,0]
    t2048(tab)
    for i in range(4):
      for k in range(4):
        if act[0]==tab[i][k] or act[1]==tab[k][i] or tab[i][k]==0:canmove=1
        act=[tab[i][k],tab[k][i]]
      act=[0,0]
    if not canmove:break
    col=(max(0,150-30*(int(log(score+0.01,2)*0.77))),150,max(0,int(log(score+0.01,2)*0.77)*30-150))
    draw_string(str(score),1,1,col)
    while not (keydown(0) or keydown(1) or keydown(2) or keydown(3)):1
    moved=[]
    tr=False
    if keydown(1) or keydown(2):#up/down
      if keydown(1):
        key=1
        key2=0
      else:
        key=-1
        key2=-1
      for k in range(4):
        act=[0,-1]
        for i in range(0-3*key2,4+5*key2,key):
          if tab[i][k]==act[0] and not act[0]==0:
            tab[act[1]][k]=0
            tab[i][k]=act[0]*2
            score=score+act[0]*2
            tr=True
            act=[0,-1]
          else:
            if not tab[i][k]==0:act=[tab[i][k],i]
        for z in range(3):
          for i in range(3+3*key2,0-3*key2,-key):
            if tab[i-key][k]==0 and not tab[i][k]==0:
              tab[i-key][k]=tab[i][k]
              tab[i][k]=0
              moved.append([i,k])
    if keydown(0) or keydown(3):#left/right
      if keydown(0):
        key=1
        key2=0
      else:
        key=-1
        key2=-1
      for i in range(4):
        act=[0,-1]
        for k in range(0-3*key2,4+5*key2,key):
          if tab[i][k]==act[0] and not act[0]==0:
            tab[i][act[1]]=0
            tab[i][k]=act[0]*2
            score=score+act[0]*2
            tr=True
            act=[0,-1]
          else:
            if not tab[i][k]==0:act=[tab[i][k],k]
        for z in range(3):
          for k in range(3+3*key2,0-3*key2,-key):
            if tab[i][k-key]==0 and not tab[i][k]==0:
              tab[i][k-key]=tab[i][k]
              tab[i][k]=0
              moved.append([i,k])
    while keydown(0) or keydown(1) or keydown(2) or keydown(3):1
    if len(moved)==0:canspawn=False
    else:canspawn=True
  draw_string(str(score),1,1,(255,0,0))
  draw_string("Game over",114,1)
  print("Score:"+str(score))
p2048()