from matplotlib.pyplot import *
from math import *

g=9.81

def x(t,v_0,alpha):
  return v_0*cos(alpha)*t
def y(t,v_0,alpha,h_0):
  return -0.5*g*t**2+v_0*sin(alpha)*t+h_0

def vx(v_0,alpha):
  return v_0*cos(alpha)
def vy(t,v_0,alpha):
  return -g*t+v_0*sin(alpha)

def t_max(v_0,alpha,h_0):
  return (v_0*sin(alpha)+sqrt((v_0**2)*(sin(alpha)**2)+2*g*h_0))/g

def simulation(v_0=15,alpha=pi/4,h_0=2):
  tMax=t_max(v_0,alpha,h_0)
  accuracy=1/10**(floor(log10(tMax))-1)
  T_MAX=floor(tMax*accuracy)+1
  X=[x(t/accuracy,v_0,alpha) for t in range(T_MAX)]
  Y=[y(t/accuracy,v_0,alpha,h_0) for t in range(T_MAX)]
  VX=[vx(v_0,alpha) for t in range(T_MAX)]
  VY=[vy(t/accuracy,v_0,alpha) for t in range(T_MAX)]
  for i in range(T_MAX):
    arrow(X[i],Y[i],VX[i]/accuracy,VY[i]/accuracy)
  grid()
  show()

#Executer le script
simulation()