# Hello, this is my trial to code tetrisimport pygame
import pygame
import random
#Initialize pygame
pygame.init()

#create the window
a = 400
b = 600
win = pygame.display.set_mode((a,b))
pygame.display.set_caption('Tetris')

# # this grid is too slow
# def drawGrid():
#     bs = delta
#     for xx in range(a):
#         for yy in range(b):
#             rect = pygame.Rect(xx*bs,yy*bs,bs,bs)
#             pygame.draw.rect(win, (40,10,50), rect,2)

timer2 = 0
clock = pygame.time.Clock()

run = True
RUNNING, PAUSE = 0,1
state = RUNNING
bar = [20,80]
delta = 20

xf,yf,wf,hf = [[],[],[],[]]

while run:
    x = a//2
    y = 0
    w = bar[0]
    h = bar[1]
    gio = {}
    if len(xf) >= 1:
        print(yf)
        for z in range(b-delta,min(yf)-delta,-delta):
            gio[z] = []
            for i in range(len(xf)):
                if yf[i]+hf[i] >= z:
                    gio[z].append(range(xf[i],xf[i]+wf[i],delta))
        
    terra = True
    while terra:
        
        win.fill((100,0,40))
        pygame.time.delay(60)
        pygame.draw.rect(win, (255,0,0), (x,y,w,h))
        if len(xf) >= 1:
            for ii in range(len(xf)):
                pygame.draw.rect(win, (255,0,0), (xf[ii],yf[ii],wf[ii],hf[ii]))        

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

        if timer2 > 1000: 
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
                for i in range(len(gio[z])):
                    for j in range(x,x+w,delta):
                        if j in gio[z][i]:                            
                            if y >= b - delta - h - hf[i]:
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
            pygame.draw.rect(win, (40,10,50), (0,0,a,b), 2*delta)
            pygame.display.update()
        

pygame.quit()



