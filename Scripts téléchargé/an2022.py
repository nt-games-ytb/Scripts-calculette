from kandinsky import draw_string, fill_rect
from ion import keydown,KEY_UP,KEY_DOWN
from time import sleep

nbjMois = "303232332323"
jSem = "LMmJVSD"
mois = "Janv,Fev, Mars,Avril,Mai,Juin,Juill,Aout,Sept,Oct,Nov,Dec".split(',')

def aff(d):
    nb = 0
    v = 5
    for i in range(d): v += int(nbjMois[i])
    v %= 7
    while nb < 2:
        m = d + nb
        for i,js in enumerate(jSem):
            draw_string(js,10 + 30 * i, 5 + 110 * nb)
        l = 1
        for j in range(28 + int(nbjMois[m])):
            pos = jSem.index(jSem[v])
            draw_string(str(j + 1),10 + 30 * pos, 5 + 110 * nb + 15 * l)
            v = (v + 1) % 7
            if pos == 6: l += 1
        draw_string(mois[m], 250, 110 * nb + 30)
        nb += 1

def eff():
    fill_rect(0,0,320,222,(255,255,255))
    sleep(.2)

def key():
  while True:
    for (i, k) in enumerate([KEY_UP,KEY_DOWN]):
      if keydown(k): return 2 * i - 1

d = 0
while True:
    aff(d)
    t = key()
    d = (d + 2 * t) % 12
    eff()