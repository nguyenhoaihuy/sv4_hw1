from s4vsprite import s4vSprite
from const import *

def collidedBelow(player, objs):
    isCollided = False
    for obj in objs:
        while player.isCollidedWith(obj):
            player.y -= 2
            isCollided = True
    return isCollided

def collidedAbove(player, objs):
    isCollided = False
    for obj in objs:
        while player.isCollidedWith(obj):
            player.y += 2
            isCollided = True
    return isCollided


class Player(s4vSprite):
    def __init__(self,x,y,img):
        #construction
        super().__init__(x,y,img)
        #set states
        self.isJump = False
        self.isGoRight = False
        self.isGoLeft = False
        self.isOnGround = False
        #set jump count
        self.jumpCount = 20
        
    
    def move(self,window,grounds):
        if self.isGoLeft:
            self.isGoLeft = False
            self.x -= PLAYER_VELOCITY
            for ground in grounds:
                if self.isCollidedWith(ground):
                    self.x += PLAYER_VELOCITY
                    break
        if self.isGoRight:
            self.isGoRight = False
            self.x += PLAYER_VELOCITY
            for ground in grounds:
                if self.isCollidedWith(ground):
                    self.x -= PLAYER_VELOCITY
                    break
        
        if self.isJump: #Checking for jumping
            self.isOnGround = False
            if self.jumpCount >= -20:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= 0.07*(self.jumpCount ** 2) * 1.3 * neg
                if self.jumpCount < 0:
                    if collidedBelow(self, grounds):
                        self.isOnGround = True
                        self.isJump = False
                        self.jumpCount = 20
                else:
                    if collidedAbove(self, grounds):
                        self.jumpCount = 0
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 20
        else: #Falling
            self.y += 30
            if collidedBelow(self, grounds):
                self.isOnGround = True                                   
                    
        self.draw(window)
           
        
    def jump(self):
        if self.isOnGround: #Player need to be on grounds to jump 
            self.isJump = True
    
    def goLeft(self):
        self.isGoLeft = True
        
    def goRight(self):
        self.isGoRight = True
