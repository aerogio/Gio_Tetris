#hi This is the file for my constants!

# tetris geometric constants

delta = 20
a = 14*delta
b = 26*delta
c = 23*delta
textX = 15*delta
textY = b//2

# colors

bar = [delta, 4*delta]
ROS, dROS = (245, 10, 10), (150, 10, 10)
ORA, dORA = (255, 170, 0), (200, 100, 0)
ACQ, dACQ = (49, 149, 127), (20, 109, 97)
VER, dVER = (30, 200, 50), (10, 100, 30)
BLU, dBLU = (50, 178, 250), (0, 100, 200)
PINK, dPINK = (255,155, 164), (200,100,120)
GIA, dGIA = (200, 255, 2), (150, 200, 2)
VIO, dVIO = (60, 10, 80), (20, 0, 30) #background
NERO = (0, 0, 0)
GRI = (80, 80, 80)

class Stone:    
    def __init__(self, shape):#, dCOLOUR):
        self.shape = shape
        if self.shape == 'I':
            self.disp = [delta,4*delta]
            self.disp2 = [['u', 'dd', 'd'], ['l', 'rr', 'r']]
            self.COLOUR = BLU
            self.dCOLOUR = dBLU
            
        elif self.shape == 'T':
            self.disp = [delta, 2*delta]
            self.disp2 = [['l', 'r', 'd'], ['r', 'u', 'd'], ['l', 'r', 'u'], ['l', 'u', 'd']]
            self.COLOUR = VER
            self.dCOLOUR = dVER

        elif self.shape == 'O':
            self.disp = [delta, 2*delta]
            self.disp2 = [['r', 'dd', 'r']]
            self.COLOUR = PINK
            self.dCOLOUR = dPINK

        elif self.shape == 'S1':
            self.disp = [delta, 2*delta]
            self.disp2 = [['r', 'dd', 'l'], ['u', 'rr', 'd']]
            self.COLOUR = ROS
            self.dCOLOUR = dROS
            
        elif self.shape == 'S2':
            self.disp = [delta, 2*delta]
            self.disp2 = [['l', 'dd', 'r'], ['d', 'rr', 'u']]
            self.COLOUR = ORA
            self.dCOLOUR = dORA

        elif self.shape == 'L1':
            self.disp = [delta, 2*delta]
            self.disp2 = [['u', 'rr', 'r'], ['d', 'uu', 'r'], ['l', 'rr', 'd'], ['u', 'dd', 'l']]
            self.COLOUR = ACQ
            self.dCOLOUR = dACQ

        elif self.shape == 'L2':
            self.disp = [delta, 2*delta]
            self.disp2 = [['l', 'rr', 'u'], ['u', 'dd', 'r'], ['d', 'rr', 'r'], ['l', 'dd', 'd']]
            self.COLOUR = GIA
            self.dCOLOUR = dGIA            
            
        self.AD = 0
        self.w = self.disp[0]
        self.h = self.disp[1]

# for d in range(3):
#     if sto.disp2[sto.AD][d] == 0:
#         x2 -= delta
#     elif sto.disp2[sto.AD][d] == 1:
#         y2 += delta
#     elif sto.disp2[sto.AD][d] == -1:
#         y2 -= delta
#         x2 += delta
#     elif sto.disp2[sto.AD][d] == -2:
#         y2 -= delta
#     elif sto.disp2[sto.AD][d] == 2:
#         y2 += delta
#         x2 += delta
#     pygame.draw.rect(win, sto.COLOUR, (x2, y2, delta, delta))


    
    
    

# def stoneI():
#     if Stone.shape is 'I':
#         sh = [delta,4*delta]
#     else:
#         print('error')
#     return sh

    
