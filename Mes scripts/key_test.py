#Modules
from math import *
from kandinsky import *
from ion import *

def test1():
  activer = False
  while activer == False:
    if keydown(KEY_RIGHT): #or keydown(KEY_DOWN):
      print("b")
      activer = True
    else:
      print("a")
      
def test2():
  bouton = input()
  if bouton == keydown(KEY_RIGHT): #or keydown(KEY_DOWN):
    print("a")
  else:
    print("b")
    
def showInput():
  inputReturn = input()
  print(inputReturn)
  return inputReturn
    
showInput()
test1()
test2()