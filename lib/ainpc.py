from npc import NPC
from const import *
from s4vsprite import s4vSprite
black = (0,0,0)
white = (255,255,255)
class AiNPC(NPC):
    def __init__(self):
        super().__init__()
        self.custom = s4vSprite(NPC_X, NPC_Y, AI_IMG)

    def congrat(self,window):
        if self.custom != None:
            self.custom.draw(window)
        def drawTalkBox():
            width = WIDTH-20
            height = 100
            x = 10
            y = HEIGHT - 130
            pg.draw.rect(window, white, (x, y, width, height))
        drawTalkBox()
        img = font.render("[AI]: Chúc mừng bạn!!!!! <Nhấn Space>", True, black)
        window.blit(img, (20, HEIGHT - 120))
    
    def reportError(self,window):
        if self.custom != None:
            self.custom.draw(window)
        def drawTalkBox():
            width = WIDTH-20
            height = 100
            x = 10
            y = HEIGHT - 130
            pg.draw.rect(window, white, (x, y, width, height))
        drawTalkBox()
        img = font.render("[AI]: Chia buon, ban chua vuot qua thu thach! <Nhan Space>", True, black)
        window.blit(img, (20, HEIGHT - 120))

    