# Hello, this is my trial to code tetris
import pygame
import random
from constants import *

pygame.init()

win = pygame.display.set_mode((a,b))
pygame.display.set_caption('Tetris')

def drawBackground():
    win.fill(VIO)
    for row in range(delta, a-delta, delta):
        for col in range(delta+ (row % (2*delta)), b-delta, 2*delta):
            pygame.draw.rect(win, dVIO, (row, col, delta,delta))


timer2 = 0
clock = pygame.time.Clock()

run = True
RUNNING, PAUSE = 0,1
state = RUNNING


counter = 0

xf,yf,wf,hf = [[], [], [], []]

gio = {}
# jj = delta

while run:

    rcol = random.randrange(4)

    if rcol is 0:
        C, dC = VER, dVER
        dC = dVER
    elif rcol is 1:
        C, dC = ROS, dROS
    elif rcol is 2:
        C, dC = PINK, dPINK
    elif rcol is 3:
        C, dC = BLU, dBLU

    bar1 = Bar([20,80], C)

    # IT DOESN't WORK BUT I KNOW WHY, also it can be done in a better way1
    
    x = a//2
    y = delta
    w = bar1.shape[0]
    h = bar1.shape[1]

    
    if len(xf) >= 1:
        for z in range(yf[-1]+hf[-1], yf[-1], -delta):
            if z not in gio.keys():
                gio[z] = []
            for bta in range(xf[-1], xf[-1] + wf[-1], delta):
                gio[z].append(bta)
            gio[z] = sorted(gio[z])

    if len(xf) >= 1:
        for z in range(b-delta, min(yf), -delta):
            jj = delta
            keepline = True
            while keepline:
                if jj not in gio[z]:
                    keepline = False
                jj += delta
                    
                    
                if jj > a-delta:
                    keepline = False
                    counter += 1
                    for zz in range(z, min(gio.keys()), -delta):
                        gio[zz] = gio[zz-delta]
                    gio[min(gio.keys())] = [] 
                    
                    
    terra = True
    while terra:
        
        drawBackground()
        pygame.time.delay(60)
        
        if len(xf) >= 1:
            for z in range(b-delta, min(yf), -delta):
                for ii in gio[z]:
                    pygame.draw.rect(win, GRI, (ii, z-delta, delta, delta))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terra = False
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    terra = False
                elif event.key == pygame.K_p:
                    state = PAUSE
                elif event.key == pygame.K_s:
                    state = RUNNING
                    
                    
                elif event.key == pygame.K_UP and y < b - delta - max(h,w):
                    i = random.randrange(2)
                    if delta < x < a - w - delta:
                        if w < h:
                            j = -1
                        else:
                            j = 1
                        x = x + j* delta * (1+i)
                    elif x >= a - w - delta:
                        x = a - delta - h
                    h,w = w, h                    
                

        dt = clock.tick()
        timer2 = timer2 + dt

        if timer2 > 1000 - 20*counter: 
            y = y + delta
            timer2 = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > delta and y < b - h - delta:
            x = x - delta 
        if keys[pygame.K_RIGHT] and x < a - w - delta and y < b - h - delta:
            x = x + delta
        if keys[pygame.K_DOWN] and y < b - h - delta:
            y = y + delta
            
        if len(xf) >= 1:
            for z in range(b-delta,min(yf),-delta):
                for j in range(x,x+w,delta):
                    if j in gio[z]:
                        if y >= z - delta - h:
                            terra = False
                    else:
                        if y >= b - delta - h:
                            terra = False
        else:
            if y >= b - delta - h:
                terra = False

        if not terra:
            xf.append(x)
            yf.append(y)
            wf.append(w)
            hf.append(h)
            
        if state == PAUSE:
            pause_text = pygame.font.SysFont('Consolas', 32).render('Pause', True, pygame.color.Color('White'))
            win.blit(pause_text, (100, 100))
            for event in pygame.event.get():
                if event.key == pygame.K_p:
                    state = RUNNING

                    
        elif state == RUNNING:
            
            # Border
            pygame.draw.rect(win, dVIO, (0,0,a,b), 2*delta)

            # Actual tetris stone
            pygame.draw.rect(win, bar1.COLOUR, (x,y,w,h)) # HERE I WILL CHANGE, instead of drawing one rect, I can have a cycle for and draw every little square to create the shape. Also, instead of BLU I can put like shape.colour so that I create a class for every color and we automatically have the corresponding colour or dark color depending on the shape
            pygame.display.update()
    
pygame.quit()


