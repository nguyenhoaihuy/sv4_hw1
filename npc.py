import pygame as pg
from const import *
from s4vsprite import s4vSprite
black = (0,0,0)
white = (255,255,255)

class NPC:
    def __init__(self):
        self.sentences = []
        self.current_sen = 0
        self.current_word = 0
        self.count_down = 7
        self.custom = None
    
    def setConversation(self,sentences):
        self.sentences = sentences
        self.current_sen = 0
        self.current_word = 0
    
    def getConversation(self):
        return self.sentences

    def talk(self, window):
        if self.custom != None:
            self.custom.draw(window)
        def drawTalkBox():
            width = WIDTH-20
            height = 100
            x = 10
            y = HEIGHT - 130
            pg.draw.rect(window, white, (x, y, width, height))
        drawTalkBox()
        next_text = self.getNextText()
        img = font.render(next_text, True, black)
        window.blit(img, (20, HEIGHT - 120))
        if self.current_sen < len(self.sentences) and self.current_word == len(self.sentences[self.current_sen]):
            self.current_word = 0
            self.current_sen += 1
            return True
        else:
            return False

    def getNextText(self):
        next_text = ""
        self.countDown()
        if self.count_down == 0:
            if self.current_sen < len(self.sentences):
                self.current_word += 1
            self.count_down = 10
        
        if self.current_sen < len(self.sentences) and self.current_word < len(self.sentences[self.current_sen]):
            next_text = self.sentences[self.current_sen][:self.current_word+1]
        return next_text


    def isFinishedTalking(self):
        if self.current_sen == len(self.sentences):
            return True
        return False

    def countDown(self):
        if self.count_down > 0:
            self.count_down -= 1
        else:
            self.count_down = 7

    def getSentenceNum(self):
        return self.current_sen