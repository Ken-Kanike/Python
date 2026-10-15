import math
from turtle import *

def hearta(self):
    return 15*math.sin(self)**3

def heartb(self):
    return 12*math.cos(self)-5*\
        math.cos(2*self)-2*\
        math.cos(3*self)-\
        math.cos(4*self)
speed(0)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)
done()