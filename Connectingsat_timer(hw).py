

import pgzrun
from random import randint
from time import time

WIDTH=500
HEIGHT=400

TITLE="Numerically connecting satellites"

satellites=[]
start_time=time()
lines=[]
next_satellite=0
totaltime=15


num2=8

def create_satellites():
    global start_time
    for i in range(0,num2):
        satellite=Actor("satellite")
        satellite.pos=(randint(40,WIDTH-40),randint(30,HEIGHT-30))
        satellites.append(satellite)
    start_time=time()

def draw():
    screen.blit("background",(0,0))
    num=1
    for satellite in satellites:
        screen.draw.text(str(num),(satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        num+=1
    
    for line in lines:
        screen.draw.line(line[0],line[1], (255,255,255))
    
    if next_satellite<num2:
        total_time=start_time-time()

        screen.draw.text(str(round(total_time,1)),(10,10), fontsize=30)
        if total_time<=0:
            screen.clear()
            screen.draw.text(str("Game over!"),(100,100), fontsize=60)
    
def update():
    pass

create_satellites()

def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite<num2:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos,satellites[next_satellite].pos))
            next_satellite+=1
        else:
            lines=[]
            next_satellite=0
pgzrun.go()

