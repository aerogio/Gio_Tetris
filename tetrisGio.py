# Hello, this is my trial to code tetris
import pygame
import random
from constants import *

pygame.init()
font = pygame.font.SysFont('Times New Roman', 30)
win = pygame.display.set_mode((c,b))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

# functions
def render_text(x,y):
    text = font.render('L E V E L', True, PINK)
    level = font.render(str(counter), True, PINK)
    win.blit(text, (x,y))
    win.blit(level, (x+50,y+50))

def drawBackground():
    win.fill(VIO)
    pygame.draw.rect(win,dVIO, (a, 0, c-a,b)) 
    for row in range(delta, a-delta, delta):
        for col in range(delta+ (row % (2*delta)), b-delta, 2*delta):
            pygame.draw.rect(win, dVIO, (row, col, delta,delta))

def randomclass(possibleShapes):
    random.shuffle(possibleShapes)
    return possibleShapes[0]

def createstone(x, y, sto):
    pygame.draw.rect(win, sto.COLOUR, (x, y, delta, delta))
    xtmp = x2 = x
    ytmp = y2 = y
    for d in range(3):
        if sto.disp2[sto.AD][d] == 'l':
            x2 -= delta
        elif sto.disp2[sto.AD][d] == 'r':
            x2 += delta
        elif sto.disp2[sto.AD][d] == 'rr':
            x2 += delta
            xtmp = x2
        elif sto.disp2[sto.AD][d] == 'u':
            y2 -= delta
        elif sto.disp2[sto.AD][d] == 'uu':
            y2 -= delta
            ytmp = y2
        elif sto.disp2[sto.AD][d] == 'd':
            y2 += delta
        elif sto.disp2[sto.AD][d] == 'dd':
            y2 += delta
            ytmp = y2
        pygame.draw.rect(win, sto.COLOUR, (x2, y2, delta, delta))
        x2 = xtmp
        y2 = ytmp
        
PS = ['I', 'T']
PS = ['I']
#PS = ['I','T','S1','S2','L1','L2','O']

def randomcolor(x):
    RCOL = random.randrange(x)
    if RCOL == 0:
        C, dC = VER, dVER
    elif RCOL == 1:
        C, dC = ROS, dROS
    elif RCOL == 2:
        C, dC = PINK, dPINK
    elif RCOL == 3:
        C, dC = BLU, dBLU
    return C

def endgame(x,y):
    global run, aria
    if 2*delta in gio.keys():
        font = pygame.font.SysFont('Times New Roman', 60)
        endtext = font.render('GAMEOVER', True, PINK)
        win.blit(endtext, (textX-200,textY+100))
        run = False
        aria = False
    return run, aria

def pieceextremes(x, y, sto):
    ymax = ymin = y
    xmax = xmin = x
    for i in sto.disp2[sto.AD]:
        if i.startswith('d'):
            ymax += delta
        elif i.startswith('u'):
            ymin -= delta
        elif i.startswith('l'):
            xmin -= delta
        elif i.startswith('r'):
            xmax += delta
    return xmin, xmax, ymin, ymax

#variable inizialization
timer = 0
run = True
RUNNING, PAUSE = 0,1
state = RUNNING
counter = 0
xf, yf, wf, hf = [[], [], [], []]
gio = {}

piece0 = Stone(randomclass(PS))
piece1 = piece0

while run:

    piece0 = piece1
    C = randomcolor(4)
    piece1 = Stone(randomclass(PS))
    
    #starting position
    x = a//2
    y = delta
    w = piece0.w
    h = piece0.h

    if len(xf) >= 1:
        for z in range(yf[-1]+hf[-1], yf[-1], -delta):
            if z not in gio.keys():
                gio[z] = []
            for bta in range(xf[-1], xf[-1] + wf[-1], delta):
                gio[z].append(bta)
            gio[z] = sorted(gio[z])
            
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

    aria = True
    while aria:
    
        drawBackground()
        pygame.time.delay(70)
        dt = clock.tick()
        timer = timer + dt
        if timer > 1000 - 20*counter and state == RUNNING: 
            y = y + delta
            timer = 0

        # to avoid contact with gio grey stones
        lll = rrr = True
        for hh in range (y,y+h+delta):
            if hh in gio.keys():
                for xx in gio[hh]:
                    if 0 < xx-x <= delta:
                        rrr = False
                    elif 0 < x-xx <= delta:
                        lll = False
        
        if len(xf) >= 1:
            for z in range(b-delta, min(yf), -delta):
                for ii in gio[z]:
                    pygame.draw.rect(win, GRI, (ii, z-delta, delta, delta))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aria = run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    aria = False
                elif event.key == pygame.K_p:
                    state = PAUSE
                elif event.key == pygame.K_s:
                    state = RUNNING                    
                    
                elif event.key == pygame.K_UP and y < b - delta - max(h,w) and lll is True and rrr is True:
                    if piece0.AD < len(piece0.disp2) - 1:
                        piece0.AD += 1
                    else:
                        piece0.AD = 0
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
                
        
            
        xmin, xmax, ymin, ymax = pieceextremes(x, y, piece0)
        # this avoid going outside
        if xmin < delta:
            x += delta

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and xmin > delta and ymax < b - delta and lll is True:
            x = x - delta    
        if keys[pygame.K_RIGHT] and xmax < a - 2* delta and ymax < b - delta and rrr is True:
            x = x + delta
        if keys[pygame.K_DOWN] and ymax < b - delta:
            y = y + delta


        if len(xf) >= 1:
            for z in range(b-delta,min(yf),-delta):
                for j in range(x,x+w,delta):
                    if j in gio[z]:
                        if ymax + delta >= z - 2* delta:
                            aria = False
                    else:
                        if ymax + delta >= b - 2*delta:
                            aria = False
        else:
            if ymax + delta >= b - 2*delta:
                aria = False
        
        if not aria:
            xf.append(x)
            yf.append(y)
            wf.append(w)
            hf.append(h)
        
        if state == PAUSE:
            pause_text = pygame.font.SysFont('Times New Roman', 32).render('GAME IS PAUSED', True, pygame.color.Color('White'))
            win.blit(pause_text, (a//2, c//2))
            pygame.display.update()
            
        elif state == RUNNING:
            # Border
            pygame.draw.rect(win, dVIO, (0,0,a,b), 2*delta)
            # Next stone
            createstone(textX+50, b//4, piece1)
            # Actual tetris stone
            createstone(x, y, piece0)
            render_text(textX, textY)
            run, aria = endgame(textX-200, textY+100)
            pygame.display.update()

pygame.quit()


