import pygame as pg
import time
from random import randint
from challenges.base_challenge import BaseChallenge
from const import *


red = (255,0,0)
white = (255,255,255)

class Lecture11(BaseChallenge):

    def __init__(self, student_solution):
        super().__init__(student_solution)
        self.ai.setConversation(["[AI]: Tra loi cau hoi sau de vuot qua thu thach","[AI]: Ban ten gi?"])
        self.player_npc.setConversation(["[Trau]: Minh da san sang"])
        self.count = 0
        self.current_count = 0
        self.level = 5
        self.count = self.level**2
        self.student_output = student_solution()
        player_conversation = self.player_npc.getConversation()
        player_conversation.append("[Trau]: "+str(self.student_output))
        self.player_npc.setConversation

    def reset(self):
        self.__init__(self.student_solution)

    def drawOutput(self, window):
        self.state = FINISH_STATE

    def checkResult(self):
        input = [[]]
        expected_output = ["Trau"]
        actual_output = list(map(lambda args: self.student_solution(*args), input))
        return expected_output == actual_output

class Lecture12(BaseChallenge):

    def __init__(self, student_solution):
        super().__init__(student_solution)
        self.x = randint(-100, 100)
        self.y = randint(-100, 100)
        self.ai.setConversation([
            "[AI]: Tra loi cau hoi sau de vuot qua thu thach",
            f"[AI]: x = {self.x}, y = {self.y}. x + y = ?"
        ])
        self.player_npc.setConversation(["[Trau]: Minh da san sang!"])
        self.count = 0
        self.current_count = 0
        self.level = 5
        self.count = self.level**2
        self.student_output = student_solution(self.x, self.y)
        player_conversation = self.player_npc.getConversation()
        player_conversation.append("[Trau]: "+str(self.student_output))
        self.player_npc.setConversation

    def drawOutput(self, window):
        self.state = FINISH_STATE

    def checkResult(self):
        input = [[34, 56], [12, -3]]
        expected_output = [90, 9]
        actual_output = list(map(lambda args: self.student_solution(*args), input))
        return expected_output == actual_output
