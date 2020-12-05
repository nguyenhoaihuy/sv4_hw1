from s4vsprite import s4vSprite
from const import *

class Ground(s4vSprite):
    def __init__(self,x,y,img):
        #construction
        super().__init__(x,y,img)
    
    def move(self,window):
        self.draw(window)
