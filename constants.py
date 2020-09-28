#hi This is the file for my constants!

# tetris geometric constants

delta = 28
a = 14*delta
b = 23*delta
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
VIO, dVIO = (59, 61, 81), (20, 0, 30) #background
NERO = (0, 0, 0)
GRI = (100, 120, 180)

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
            self.disp2 = [['r', 'd', 'o']]
#            self.disp2 = [['uu', 'rr', 'd']]
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

