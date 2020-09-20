#hi This is the file for my constants!
#import pygame

# tetris geometric constants

delta = 20
a = 16*delta
b = 24*delta

# colors

bar = [delta, 4*delta]
ROS, dROS = (245, 10, 10), (150, 10, 10)
VER, dVER = (30, 200, 50), (10, 100, 30)
BLU, dBLU = (50, 178, 250), (0, 100, 200)
PINK, dPINK = (255,155, 164), (200,100,120)
VIO, dVIO = (60, 10, 80), (20, 0, 30) #background
NERO = (0, 0, 0)
GRI = (80, 80, 80)

class Bar:
    def __init__(self, shape, COLOUR):#, dCOLOUR):
        self.shape = shape
        self.COLOUR = COLOUR
#        self.dCOLOUR = dCOLOUR
    pass
