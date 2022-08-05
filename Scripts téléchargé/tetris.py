# Tetris NW
# par Robert V. & Fedyna K.

from ion import keydown
from kandinsky import *
from random import randint
from time import *
from math import sqrt,log

parametres = ("Jouer","Niveau","Vision","Grille","nsi.xyz")
options = (0,(1,16,42),(0,1,2,3),(0,1),0)
reglages = ["",1,2,0,""]
color = ((4<<5,6<<5,7<<5),(7<<5,4<<5,6<<5),(6<<5,7<<5,4<<5),(6<<5,6<<5,6<<5),(7<<5,6<<5,4<<5),(6<<5,4<<5,7<<5),(4<<5,7<<5,6<<5))
formes = ([(1,1,2,1)],[(1,2,1),(0,0,1)],[(0,2,1),(1,1,0)],[(2,2),(2,2)],[(1,2,1),(0,1,0)],[(1,2,1),(1,0,0)],[(1,2,0),(0,1,1)])
gl = [1,0,0]

try:
    get_keys()
    os = (192,53,53)
except:
    os = (255,183,52)

fill_rect(74,0,2,222,os)
fill_rect(246,0,2,222,os)

draw_string("TETRIS",7,2,(120,120,120))
for i in range(7):
    fill_rect(3+10*i,25,8,8,color[i])

def menu(c):
    y,p = 40,0
    score()
    for i in range(13):
        fill_rect(76+i*14,0,2,222,(240,240,240)*(reglages[3]==1)+(255,255,255)*(reglages[3]==0))
    fill_rect(248,0,72,100,(255,255,255))
    for i in parametres:
        draw_string(i,37 - len(i)*5,y,(120,120,120)*(p != c)+os*(p == c))
        if options[p] != 0:
            op = ""
            for j in options[p]:
                op += str(j)
            x = 37 - len(op)*5 - round(5*len(options[p]) / 2)
            for j in options[p]:
                draw_string(str(j),x,y+20,(196,196,196)*(j != reglages[p])+os*(j == reglages[p]))
                x += 15+10*(len(str(j))-1)
            y += 20
        p += 1
        y += 26

def nav():
    k,c = 0,0
    menu(c)
    while k != 5:
        draw_string("Lignes", 253, 138, (120, 120, 120))
        draw_string("Score", 261, 184, (120, 120, 120))
        k = getKey()
        if k in (4,52):
            engine()
        if k in (1,2):
            c = c+(k == 2) - (k == 1)
            c = c*(0 < c < len(reglages))+(len(reglages)-1)*(c < 0)
        menu(c)
        if k in (0,3):
            if reglages[c] != "":
                i = options[c].index(reglages[c])
                j = i+1*(k == 3) - 1*(k == 0)
                j = j*(0 < j < len(options[c]))+(len(options[c])-1)*(j < 0)
                reglages[c] = options[c][j]
            menu(c)

def score(li=0, i=0):
    gl[1] += li
    gl[2] += gl[0]*(25*li+25*2**max(li-1,0))*(li!=0)+gl[0]*i
    gl[0] = max(round(sqrt(gl[2] + (10 * reglages[1]) ** 2 ) / 10), reglages[1])
    fill_rect(270,108,30,22,(120, 120, 120))
    draw_string(str(gl[0]),284-5*len(str(gl[0])),110,(255,255,255),(120,120,120))
    draw_string(str(gl[1]),284-5*len(str(gl[1])),158,os)
    draw_string(str(gl[2]),284-5*len(str(gl[2])),204,os)

def rlen(l):
    return range(len(l))

def ancr(piece):
    for i in rlen(piece[1]):
        for j in rlen(piece[1][i]):
            if piece[1][i][j] == 2:
                return piece[0][0]-14*j, piece[0][1]-14*i

def getKey():
    while True:
        for i in range(53):
            if keydown(i):
                while keydown(i):
                    pass
                return i

def draw_tetro(piece,clr=-1):
    if clr == -1:
        clr = piece[2]
    x,y = ancr(piece)
    for i in rlen(piece[1]):
        for j in rlen(piece[1][i]):
            if piece[1][i][j]:
                fill_rect(x+14*j+1,y+14*i+1,12,12,clr)

def tourner(piece,s,t=0):
    if not t:
        draw_tetro(piece,(248,252,248))
    if s == "h":
        piece[1] = list(zip(*piece[1][::-1]))
    if s == "a":
        piece[1] = list(zip(*(list(i)[::-1] for i in piece[1])))
    if not t:
        draw_tetro(piece)

def move(piece,x=0,y=0):
    draw_tetro(piece, (248, 252, 248))
    piece[0][0] += x*14
    piece[0][1] += y*14
    draw_tetro(piece)

def test_rot(piece,s):
    x,y = ancr(piece)
    blocs = []
    for i in rlen(piece[1]):
        for j in rlen(piece[1][i]):
            if piece[1][i][j]:
                blocs += [[x+14*j,y+14*i]]
    tourner(piece,s,1)
    x,y = ancr(piece)
    for i in rlen(piece[1]):
        for j in rlen(piece[1][i]):
            if not [j*14+x,i*14+y] in blocs:
                if not(77<=x+14*j<=231) or not(11<=y+14*i<=207) or get_pixel(x+7+14*j,y+7+14*i) != (248,252,248):
                    tourner(piece,"a"*(s=="h")+"h"*(s=="a"),1)
                    return 1
    tourner(piece,"a"*(s=="h")+"h"*(s=="a"),1)
    return 0

def collision(d,piece):
    x,y = ancr(piece)
    for i in rlen(piece[1]):
        for j in rlen(piece[1][i]):
            if piece[1][i][j]:
                if d in (0,3) and ((0<=j+(d==3)-(d==0)<=len(piece[1][i])-1 and not piece[1][i][j+(d==3)-(d==0)]) or (j,d) in ((0,0),(len(piece[1][i])-1,3))):
                    if get_pixel(x+7+14*(j+(d==3)-(d==0)),y+7+14*i) != (248,252,248) or x+((j+1)*14)*(d!=0) in [77,245]:
                        return 1
                if d == 2 and ((i != len(piece[1])-1 and not piece[1][i+1][j]) or (i == len(piece[1])-1 and piece[1][i][j])):
                    if get_pixel(x+7+14*j,y+7+14*(i+1)) != (248,252,248) or y+i*14 == 207:
                        return 1
    return 0

def engine():
    global gl
    if reglages[2]:
        tetrominos = []
        for i in range(reglages[2]):
            chx = randint(0, 6)
            tetrominos += [[[280, 2+i*32], formes[chx], color[chx]]]
    while get_pixel(154,18) == (248,252,248):
        chx = randint(0, 6)
        if reglages[2]:
            for tet in tetrominos:
                draw_tetro(tet,(248,252,248))
            tetromino = [[147, 11],tetrominos[0][1],tetrominos[0][2]]
            tetrominos = [tetrominos[i+1] for i in range(reglages[2]-1)] + [[[0, 0], formes[chx], color[chx]]]
            for i in range(reglages[2]):
                tetrominos[i][0] = [280, 2+i*32]
            for tet in tetrominos:
                draw_tetro(tet)
        else:
            tetromino = [[147, 11], formes[chx], color[chx]]
        draw_tetro(tetromino)
        chute = 0.120
        while 1:
            depart = monotonic()
            while monotonic() < depart+round(-0.1945871*log(gl[0])+1.01122,3):
                if keydown(0) and not collision(0, tetromino):
                    move(tetromino, x=-1)
                    sleep(0.120)
                if keydown(3) and not collision(3,tetromino):
                    move(tetromino,x=1)
                    sleep(0.120)
                if keydown(2):
                    sleep(chute)
                    chute /= 2
                    score(i=1)
                    break
                chute = 0.120
                if keydown(16) and not test_rot(tetromino,"h"):
                    sleep(0.160)
                    tourner(tetromino,"h")
                if keydown(17) and not test_rot(tetromino,"a"):
                    sleep(0.160)
                    tourner(tetromino,"a")
            if collision(2,tetromino):
                break
            score(i=1)
            move(tetromino,y=1)
        lignes = []
        for i in range(214,4,-14):
            verif = 0
            for j in range(84,252,14):
                verif += (get_pixel(j,i) != (248,252,248)) + 2*(get_pixel(j,i) == (248,252,248))
            if verif == 12:
                lignes += [i-7]
            if verif == 24:
                stop = i-7
                break
        if lignes:
            score(li=len(lignes))
            for c in range(7):
                for i in lignes:
                    for j in range(77,245,14):
                        fill_rect(j+1,i+1,12,12,not c%2 and (248,252,248) or os)
                sleep(0.2*round(-0.1945871*log(gl[0])+1.01122,3))
            lignes = [lignes[i]+i*14 for i in rlen(lignes)]
            for i in lignes:
                for y in range(i,stop-14,-14):
                    for x in range(77,245,14):
                        fill_rect(x+1,y+1,12,12,get_pixel(x+7,y-7))
    fill_rect(120,100,80,42,os)
    draw_string("PERDU",135,102,(248,252,248),os)
    draw_string(str(gl[2]),160-5*len(str(gl[2])),122,(248,252,248),os)
    getKey()
    gl = [1, 0, 0]
    fill_rect(77, 11, 168, 210, (248, 252, 248))
    fill_rect(248, 0, 72, 222, (248, 252, 248))

nav()