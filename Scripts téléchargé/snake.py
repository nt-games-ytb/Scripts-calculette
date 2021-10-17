from kandinsky import *
from time import sleep
from ion import *
from random import randint

config = {}
# try: from snake_config import config
# except: pass

class Snake:
  def __init__(self, config, high_score=0):
    self.imported_config = config
    self.high_score = high_score
    self.init_snk()
    self.show_score()
    self.start()

  def set_config(self):
    self.x,self.y=160,110
    self.init_len=3
    self.body=[(self.x,self.y)]
    self.sleep=0.01
    self.decrement=0.0003
    self.inc=1
    self.direction="up"
    self.tdirection="up"

    self.brd_co = (255,0,0)
    self.bg_co = (255,255,255)
    self.snk_co = (100,255,100)
    self.fd_co = (255,100,100)
    
    for key, value in self.imported_config.items():
      setattr(self, key, value)

  def init_snk(self):
    self.set_config()
    self.len = self.init_len
    self.eat = []

    fill_rect(0,0,320,222,self.bg_co)
    fill_rect(0,0,320,6,self.brd_co)
    fill_rect(0,0,5,222,self.brd_co)
    fill_rect(320-5,0,5,222,self.brd_co)
    fill_rect(0,222-6,320,6,self.brd_co)

    for _ in range(3):
      self.spawn_food()    
    
    self.show_score()

  def spawn_food(self):
    while True:      
      fx=randint(10,310)
      fy=randint(10,210)
      fx-=fx%10
      fy-=fy%10
      if (fx, fy) not in self.body:
        break
    fill_rect(int(fx-10/2),int(fy-10/2)+1,int(10),int(10),self.fd_co)

    self.eat.append((fx, fy))

  def show_score(self,sx=205,sy=6):
    draw_string("Score : {:0>2}".format(self.len-self.init_len),sx,sy)  

  def start(self):
    sub_iter = lambda i1, i2: tuple(v1-v2 for v1, v2 in zip(i1, i2))
    
    while 1:
      if self.len < len(self.body):
        self.body.pop(0)
      if len(self.body) > self.init_len-1:
        dx, dy = self.body[0]
        
        av=abs(self.x-self.body[-1][0]) or abs(self.y-self.body[-1][1])
                
        ddir = sub_iter(self.body[0], self.body[1])
        l,L=self.inc, self.inc
        if ddir[0] < 0:#g
          L=10
          dx+=av
        if ddir[0] > 0:#d
          L=10
          dx+=10-av-1
        if ddir[1] < 0:#b
          l=10
          dy+=av
        if ddir[1] > 0:#h
          l=10
          dy+=10-av-1
        fill_rect(int(dx-10/2),int(dy-10/2)+1,l,L,self.bg_co)
          
      fill_rect(int(self.x-10/2),int(self.y-10/2)+1,int(10),int(10),self.snk_co)
      sleep(self.sleep)

      if keydown(KEY_HOME):
        while keydown(KEY_HOME): pass
        while not keydown(KEY_HOME): pass
        while keydown(KEY_HOME): pass


      if keydown(KEY_UP):
        self.tdirection="up"
      if keydown(KEY_DOWN):
        self.tdirection="down"
      if keydown(KEY_RIGHT):
        self.tdirection="right"
      if keydown(KEY_LEFT):
        self.tdirection="left"

      if self.tdirection=="up" and self.direction!="down" and self.x%10==0:
        self.direction="up"
      if self.tdirection=="down" and self.direction!="up" and self.x%10==0:
        self.direction="down"
      if self.tdirection=="right" and self.direction!="left" and self.y%10==0:
        self.direction="right"
      if self.tdirection=="left" and self.direction!="right" and self.y%10==0:
        self.direction="left"

      if self.direction=="up":
        self.y-=self.inc
      if self.direction=="down":
        self.y+=self.inc
      if self.direction=="right":
        self.x+=self.inc
      if self.direction=="left":
        self.x-=self.inc

      if self.x%10==0 and self.y%10==0:
        self.body.append((self.x,self.y))
        if (self.x,self.y) in self.eat:
          self.len+=1
          del self.eat[self.eat.index((self.x,self.y))]
      
          self.spawn_food()
          self.show_score()
          if self.sleep>self.decrement:
            self.sleep-=self.decrement
          elif self.inc==1:
            self.sleep=0.01
            self.inc+=1

        elif (self.x,self.y) in self.body[:-1] or not 0<self.x<320 or not 0<self.y<220:
          fill_rect(5,6,310,210,self.bg_co)
          draw_string("Game Over",120,100)
          draw_string("Press EXE to play again",55,120)
          draw_string("Press OFF to play exit",55,137)

          self.high_score=max(self.len - self.init_len, self.high_score)
          draw_string("Highscore : "+str(self.high_score) ,80,190)
  
          self.show_score(120,170)
          while 1 :
            if keydown(KEY_EXE):
              break
            if keydown(KEY_ONOFF):
              return
            sleep(0.01)

          self.init_snk()


Snake(config, high_score=74)