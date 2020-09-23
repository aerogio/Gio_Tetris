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
VER, dVER = (30, 200, 50), (10, 100, 30)
BLU, dBLU = (50, 178, 250), (0, 100, 200)
PINK, dPINK = (255,155, 164), (200,100,120)
VIO, dVIO = (60, 10, 80), (20, 0, 30) #background
NERO = (0, 0, 0)
GRI = (80, 80, 80)

class Stone:
    def __init__(self, shape):#, dCOLOUR):
        self.shape = shape
#        self.COLOUR = COLOUR
        
        if self.shape == 'I':
            self.disp = [delta,4*delta]
            self.disp2 = [1, 1, 1]
            self.COLOUR = BLU
        elif self.shape == 'T':
            self.disp = [delta,2*delta]
            self.disp2 = [0, 1, -1]
            self.COLOUR = VER
        self.w = self.disp[0]
        self.h = self.disp[1]

#        self.dCOLOUR = dCOLOUR
# def designstone(x): DO IT TOMORROW
    
    

# def stoneI():
#     if Stone.shape is 'I':
#         sh = [delta,4*delta]
#     else:
#         print('error')
#     return sh

    
