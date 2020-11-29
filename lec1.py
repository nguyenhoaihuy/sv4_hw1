import pygame as pg
import time
from challenge import Challenge
from student import *
from const import *
red = (255,0,0)
white = (255,255,255)
class Lecture11(Challenge):    
    def __init__(self):
        super().__init__()
        self.ai.setConversation(["[AI]: Tra loi cau hoi sau de vuot qua thu thach","[AI]: Ban ten gi"])
        self.player_npc.setConversation(["[Trau]: Minh biet roi"])
        self.count = 0
        self.current_count = 0
        self.level = 5
        self.count = self.level**2
        self.student_output = lec1_challenge1_implementation()
        player_conversation = self.player_npc.getConversation()
        player_conversation.append("[Trau]: "+str(self.student_output))
        self.player_npc.setConversation

    def reset(self):
        self.__init__()

    def drawOutput(self, window):
        self.state = FINISH_STATE

    def checkResult(self):
        if len(self.student_output) != 0 and self.student_output != "Minh chua duoc dat ten":
            return True
        return False

    def lec11_solution(self, level):
        pass


class Lecture12(Challenge):    
    def __init__(self):
        super().__init__()
        self.ai.setConversation(["[AI]: Tra loi cau hoi sau de vuot qua thu thach","[AI]: 34 + 56 = ?"])
        self.player_npc.setConversation(["[Trau]: Minh biet roi"])
        self.count = 0
        self.current_count = 0
        self.level = 5
        self.count = self.level**2
        self.student_output = lec1_challenge2_implementation(34,56)
        player_conversation = self.player_npc.getConversation()
        player_conversation.append("[Trau]: "+str(self.student_output))
        self.player_npc.setConversation

    def drawOutput(self, window):
        self.state = FINISH_STATE

    def checkResult(self):
        if self.lec12_solution(34,56) == self.student_output:
            return True
        return False


    def lec12_solution(self, x, y):
        return x+y
                