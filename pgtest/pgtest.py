#!/bin/python
import random
import curses
import sys
import signal
import time
width=128
height=24
w = curses.initscr()
signal.signal(signal.SIGINT, exit)
def run():
    line=[]
    i=0

    line.append(0.5)
    line.append(0.5)
    move=1
    roughness=2
    # while True:
    i=0
    while(len(line)<width):
        maxi=len(line)-1
    # for i in range(0,maxi):

        num=(line[i]+line[i+1])/2
        num+=num*(random.uniform(-0.5,0.5)*(move*roughness))
        line.insert(i+1,num)
        i+=2
        if i>maxi:
            i=0
            move/=2
    # while len(line) > width:
        # j=int(len(line)/2)
        # line[j]=(line[j]+line[j+1])/2
        # line.pop(j+1)
    drawline(line)
    # line.pop(0)
    # line.pop(len(line)-1)
    # input("Press Enter to continue...")
    # time.sleep(0.5)
def drawline(line):
    canvas={}
    x=-1
    for point in line:
        x+=1
        try:
            canvas=drawpoint(canvas,x,point)
        except KeyError:
            pass
    displaycanvas(canvas)

def drawpoint(canvas,x,y):
    pointx=int(width*x)
    pointy=int(height*y)
    pointx=x
    try:
        canvas[pointx][pointy]="#"
    except KeyError:
        canvas[pointx]={}
        canvas[pointx][pointy]="#"

    return canvas

def displaycanvas(canvas):
    output=""
    for i in range(0,height):
        for j in range(0,width):
            try:
                char=canvas[j][i]
            except KeyError:
                char="."
            output="{}{}".format(output,char)
        output="{}{}".format(output,"\n")
    w.clear()
    w.addstr(output)
    w.refresh()
def exit(signal,frame):
    curses.endwin()
    sys.exit()
