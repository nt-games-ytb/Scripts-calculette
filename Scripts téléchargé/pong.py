"""
PONG for numWorks
2020 - original code by Fime
dedicace a la classe des 2nde7 de STEX
since 20 september 2020
"""

from kandinsky import *
from ion import *
from random import randint
from time import *

#colors
bG_color=[60,60,60]
ball_color=[255,200,0]
line_color=[255,255,255]
pad_color=[255,255,255]

#graphics
ballDetail,lineDetail,padDetail=0,0,0

#game preferences
mode=0
maxScore=2
difficulty=1
hardMode=0
events=0

#game engine
def game(mode, maxScore,difficulty,events,hardMode,bG_color, ball_color, pad_color, line_color,ballDetail,padDetail,lineDetail):
    
    #def ball vars
    ballSize=5
    ballPosition=[50,0]
    ballSpeed=[2,2]
    ballLegacy=[50,0,5]
    
    #def pads vars
    pad1Position=70
    pad2Position=60
    padSize=20
    minPosition=0+padSize
    maxPosition=220-padSize
    
    #draw background
    fill_rect(0,0,320,240,bG_color)
    
    #time instanciation
    originTime=int(monotonic()-1)
    eventMessageTime=0
    
    #game vars
    bounces=0
    p1score=0
    p2score=0
    initDifficulty=difficulty
    
    end=False
    
    #developpement vars
    frameCount=0
    fd=monotonic()
    spf=0.016
    
    #transiton before playing
    transition()
    
    #game loop
    while end==False:
      
      ###########draw ball
      
      fill_rect(ballPosition[0],ballPosition[1],ballSize,ballSize,ball_color)
      if ballDetail:#draw details
        fill_rect(ballPosition[0]+1,ballPosition[1]+1,ballSize-2,ballSize-2,bG_color)
      
      ballLegacy=ballPosition[0],ballPosition[1],ballSize #save ball legacy
      
      #fps
      frameCount+=1
      fps= int(float(frameCount)/(float(monotonic())-originTime)) #=frames since playing/seconds sine playing
      
      ###########controls    
      #p1
      if (keydown(KEY_UP)) and (pad1Position > minPosition):
          pad1Position -= 5
      elif (keydown(KEY_DOWN)) and (pad1Position < maxPosition):
          pad1Position += 5
      
      #solo mode
      if mode==0:
        pad2Position = pad1Position
      
      
      #vs computer mode
      if mode==1:
        if (pad2Position-ballPosition[1]>padSize+15-2*difficulty) and (pad2Position > minPosition):
          pad2Position -= difficulty+3
        elif (pad2Position-ballPosition[1]<-(padSize+15-2*difficulty)) and (pad2Position < maxPosition):
          pad2Position += difficulty+3
        
      #vs p2 mode
      if mode==2:
        if (keydown(KEY_MULTIPLICATION)) and (pad2Position > minPosition):
          pad2Position -= 5
        elif (keydown(KEY_PLUS)) and (pad2Position < maxPosition):
          pad2Position += 5
      
      #events
      if randint(0,1000)==10 and events:
        
        draw_string("warning",120,100)
        eventMessageTime= int(monotonic())
        
        if randint(0,1)==1 and padSize!=10:
          padSize-=10
          minPosition=0+padSize
          maxPosition=222-padSize
        else:    
          if randint(0,1)==1 and ballSize<10:
            ballSize+=2
          elif ballSize>4:
            ballSize-=2
      
      if (int(monotonic())-eventMessageTime)==2:
        fill_rect(120,100,70,20,bG_color)
      
      #draw middle line
      fill_rect(155,0,5,222,line_color)
      if lineDetail:
        for i in range(1,220,20):
          fill_rect(156,i,3,19,bG_color)
      
      #draw pads
      #1
      for i in [20,295]:
        j = pad1Position if i==20 else pad2Position
        fill_rect(i,j-padSize,5,2*padSize,pad_color)
        fill_rect(i,0,5,0+(j-padSize),bG_color)
        fill_rect(i,j+padSize,5,222-(padSize+j),bG_color)
        if padDetail:
          fill_rect(i+1,j+1-padSize,3,2*padSize-2,bG_color)
        
      #bounces on edges
      if ballPosition[1]<0 or ballPosition[1]>222-ballSize:
        if hardMode:
          ballPosition[1]=220-ballSize if ballPosition[1]<0 else 0
        else:
          ballPosition[1]=0 if ballPosition[1]<0 else 222-ballSize 
          ballSpeed[1]=-(ballSpeed[1])
        
      
      if (ballPosition[0]>315) or (ballPosition[0]<0):
        if (ballPosition[0]>315):
          p1score+=1
        if (ballPosition[0]<0):
          p2score+=1
        difficulty+=1
        pad1Position=110
        pad2Position=110
        ballPosition=[160,110] 
        ballSpeed = [2,2] if ballPosition[1]<0 else [-2,-2]
        if mode==0 or p1score==maxScore or p2score==maxScore:
          end=True
        else:
          ballOut()    
      
      #pad hitBox
      if (ballPosition[0]>295-ballSize) and (ballPosition[0]<300):
        if (ballPosition[1]>pad2Position-padSize-ballSize)and (ballPosition[1]<pad2Position+padSize+ballSize):
          ballSpeed[0]=-ballSpeed[0]
          ballSpeed[1]+=(ballPosition[1]-pad2Position)%3+difficulty%2+randint(-1,1)
          ballPosition[0]= 295-ballSize
          bounces+=1
      
      if (ballPosition[0]>20)and (ballPosition[0]<27):
        if (ballPosition[1]>pad1Position-padSize-ballSize)and (ballPosition[1]<pad1Position+padSize+ballSize):
          ballSpeed[0]=-ballSpeed[0]
          ballSpeed[1]+=(ballPosition[1]-pad2Position)%3+difficulty%2+randint(-1,1)
          ballPosition[0]=26
          bounces+=1
      
      
      #text
      if mode!=0:
        draw_string(str(p1score),30,10,line_color,bG_color)
        draw_string(str(p2score),180,10,line_color,bG_color)
      
      if mode==0:
        draw_string(str(bounces),30,10,line_color,bG_color)
      
      #pause
      if keydown(KEY_BACKSPACE):
        frameCount=0
        originTime=int(monotonic())
        pause()
      
      #difficulty regulator
      if frameCount==1000:
        difficulty+=1
      
      #calculate ballPosition
      ballPosition[0]+=ballSpeed[0]
      ballPosition[1]+=ballSpeed[1]
      
      while not monotonic()-fd>=spf:
        pass
      fd=monotonic()
      fill_rect(ballLegacy[0],ballLegacy[1],ballLegacy[2],ballLegacy[2],bG_color)
    
    ############## end of the loop.
    gameOver(mode,bounces,p1score,p2score)
    transition()
    mainMenu(mode,maxScore,initDifficulty,events,hardMode,ballDetail,padDetail,lineDetail)

#pause
def pause():
  while keydown(KEY_BACKSPACE):
    pass
  while not keydown(KEY_BACKSPACE):
    draw_string("paused",120,40)
    draw_string("press BACKSPACE",120,70)

  while keydown(KEY_BACKSPACE):
    pass
  fill_rect(0,0,320,220,bG_color)

#ballout          
def ballOut():
  draw_string("ball out",120,40)
  sleep(0.5)
  fill_rect(0,0,320,220,bG_color)

#game over  
def gameOver(mode,bounds,p1score,p2score):
  
  transition()
  
  #draw screen
  fill_rect(0,0,320,240,ball_color)
  fill_rect(5,5,310,210,bG_color)
  
  for j in (70,130):  
    for i in range(0,320,10):
      fill_rect(i,j,5,10,line_color)

  if mode==0:
    draw_string("game over",225,35,line_color,bG_color)
    draw_string("bounces :"+str(bounds),120,100,line_color,bG_color)
  else:
    if p1score>p2score:
      draw_string("P1 won",230,35,line_color,bG_color)
    else:
      draw_string("P2 won",230,35,line_color,bG_color)
    draw_string(str(p1score)+"-"+str(p2score),145,100,line_color,bG_color)
  
  logo(20,15,line_color,False)
  draw_string("press OK",220,180,bG_color,line_color)
  while not keydown(KEY_OK):
      pass
  while keydown(KEY_OK):
      pass      

#main menu
def mainMenu(mode,maxScore,difficulty,events,hardMode,ballDetail,padDetail,lineDetail):
  fill_rect(0,0,320,240,ball_color)
  fill_rect(5,5,310,210,bG_color)
  logo(65,20,line_color,True)
  for i in range(0,320,10):
    fill_rect(i,80,5,10,line_color)
  
  elementsType=("Btn","Lst","Btn","Btn")
  elementsValue=[None,[mode,0,2],None,None]
  elementsText=("Play",("Mode",("solo","vs bot","vs p2")),"Game settings","Video settings")
  responce = menu(60,110,ball_color,elementsType,elementsText,elementsValue)  
  
  mode=responce[1]
  
  if responce[0]:
    game(mode,maxScore,difficulty,events,hardMode,bG_color,ball_color,pad_color,line_color,ballDetail,padDetail,lineDetail)    
  if responce[2]:
    gameMenu(mode,maxScore,difficulty,events,hardMode,ballDetail,padDetail,lineDetail)
  if responce[3]:
    videoMenu(mode,maxScore,difficulty,events,hardMode,ballDetail,padDetail,lineDetail)
  
#game settings
def gameMenu(mode,maxScore,difficulty,events,hardMode,ballDetail,padDetail,lineDetail):
  fill_rect(0,0,320,240,ball_color)
  fill_rect(5,5,310,210,bG_color)
  
  elementsType=("Sld","Sld","Lst","Lst","Btn")
  elementsValue=[[maxScore,1,20],[difficulty,1,10],[events,0,1],[hardMode,0,1],None]
  elementsText=("Max score","Difficulty",("Events",("no","yes")),("Hard Mode",("no","yes")),"back")
  responce = menu(60,20,ball_color,elementsType,elementsText,elementsValue)
  
  maxScore=responce[0]
  difficulty=responce[1]
  events=responce[2]
  hardMode=responce[3]
  mainMenu(mode,maxScore,difficulty,events,hardMode,ballDetail,padDetail,lineDetail)

def videoMenu(mode,maxScore,difficulty,events,hardMode,ballDetail,padDetail,lineDetail):
  fill_rect(0,0,320,240,ball_color)
  fill_rect(5,5,310,210,bG_color)
  
  elementsType=("Lst","Lst","Lst","Btn")
  elementsValue=[[ballDetail,0,1],[padDetail,0,1],[lineDetail,0,1],None]
  elementsText=(("Ball details",("no","yes")),("Pad details",("no","yes")),("Line details",("no","yes")),"back")
  responce = menu(60,20,ball_color,elementsType,elementsText,elementsValue)
  
  ballDetail=responce[0]
  padDetail=responce[1]
  lineDetail=responce[2]
  mainMenu(mode,maxScore,difficulty,events,hardMode,ballDetail,padDetail,lineDetail)


#draw logo
def logo(x,y,line_color,line):
  #"p"
  fill_rect(x,y,10,50,line_color)
  fill_rect(x+30,y,10,20,line_color)
  fill_rect(x,y,30,10,line_color)
  fill_rect(x,y+20,30,10,line_color)
  #"o"
  fill_rect(x+50,y+10,10,30,line_color)
  fill_rect(x+80,y+10,10,30,line_color)
  fill_rect(x+60,y,30,10,line_color)
  fill_rect(x+50,y+40,30,10,line_color)
  #"n"
  fill_rect(x+100,y,10,50,line_color)
  fill_rect(x+130,y,10,50,line_color)
  fill_rect(x+110,y+10,10,10,line_color)
  fill_rect(x+120,y+20,10,10,line_color)
  #"g"
  fill_rect(x+150,y+10,10,30,line_color)
  fill_rect(x+180,y+30,10,10,line_color)
  fill_rect(x+160,y,30,10,line_color)
  fill_rect(x+150,y+40,30,10,line_color)
  fill_rect(x+170,y+20,20,10,line_color)
  #"-"
  if line: 
    fill_rect(x,y+60,190,10,line_color)

#transition between diff. screens
def transition():
  for j in (line_color,bG_color):
    for i in range(0,340,20):
      fill_rect(0,0,i,222,j)
      sleep(0.01)

#title annimation    
def annimation():
  for j in range(0,222,10):
    for i in range(0,320,10):
      fill_rect(i,j,10,10,(i-j,i-j,i-j))
      
  logo(70,80,line_color,False)
  draw_string("by FIME",70,140,line_color,"black")
  sleep(2)
  transition()


#menu
def menu(x,y,selection_color,elementsType,elementsText,elementsValue):
  
  stop=False
  select=0
  maxSelect= len(elementsText)
  
  while not stop:
    distance=0
    responce=[]
    
    if keydown(KEY_UP) and select !=0:
      while keydown(KEY_UP):
        pass
      select-=1
    elif keydown(KEY_DOWN) and select!=maxSelect-1:
      while keydown(KEY_DOWN):
        pass
      select+=1
    
    for i in range(0,maxSelect):
      
      if select==i:
        print_color=selection_color
        
        if elementsType[i]=="Btn" and i==select:
          if keydown(KEY_OK) or keydown(KEY_RIGHT):
            while keydown(KEY_OK) or keydown(KEY_RIGHT):
                pass
            elementsValue[i]=True
            stop=True
        
        elif elementsType[i]!="Btn":
          
          if keydown(KEY_RIGHT) and elementsValue[i][0]!=elementsValue[i][2]:
            while keydown(KEY_RIGHT):
              pass
            elementsValue[i][0]+=1
            fill_rect(x,y+distance,230,25,bG_color)
        
          elif keydown(KEY_LEFT) and elementsValue[i][0]!=elementsValue[i][1]:
            while keydown(KEY_LEFT):
              pass
            elementsValue[i][0]-=1
            fill_rect(x,y+distance,230,25,bG_color)
      
      else:
        print_color=line_color
      
      
      if elementsType[i]=="Lst":
        responce.append(elementsValue[i][0])
        printStr=str((elementsText[i][0])+": "+str([elementsText[i][1][elementsValue[i][0]]]))
      
      elif elementsType[i]=="Sld":
        responce.append(elementsValue[i][0])
        printStr = str(elementsText[i]+": "+str(elementsValue[i][0]))
      
      else:
        printStr=str(elementsText[i]+" →")
        responce.append(elementsValue[i])
        
      draw_string(printStr,x,y+distance,print_color,bG_color)
      distance+=25
      
  return responce

annimation()
mainMenu(mode,maxScore,difficulty,events,hardMode,ballDetail,padDetail,lineDetail)
