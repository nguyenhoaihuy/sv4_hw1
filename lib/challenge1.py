import pygame as pg
import time
from challenge import Challenge
# from playernpc import PlayerNPC
from student import *
# from ainpc import AiNPC
from const import *
red = (255,0,0)
white = (255,255,255)
class Challenge1(Challenge):    
    def __init__(self):
        super().__init__()
        self.ai.setConversation(["[AI]: Ban can ve kim tu thap cap 5","[AI]: Ve nao"])
        self.player_npc.setConversation(["[Trau]: Minh biet roi","[Trau]: Cam on"])
        self.count = 0
        self.current_count = 0
        self.level = 5
        self.count = self.level**2
        self.student_output = hw1_implementation(self.level)
    
    def reset(self):
        self.__init__()

    def drawOutput(self, window):
        width = 650
        height = 400
        x_a = 450
        y_a = 20
        level = len(self.student_output)
        margin = 5
        cube_size = (height - 20)//(level+margin)
        cube_initial_x = x_a + width//2-level*(cube_size+margin)-cube_size//2
        cube_initial_y = y_a + height-level*(cube_size+margin)-10
        pg.draw.rect(window, white, (450, 20, width, height))
        count = 0
        for row in range(len(self.student_output)):
            for col in range(len(self.student_output[row])):
                if self.student_output[row][col] == "*":
                    if self.current_count == self.count:
                        self.state = FINISH_STATE
                        pg.draw.rect(window, red, (cube_initial_x+col*(cube_size+margin), cube_initial_y+row*(cube_size+margin), cube_size, cube_size))
                        

                    elif self.current_count < self.count:
                        if count == self.current_count:
                            break
                        pg.draw.rect(window, red, (cube_initial_x+col*(cube_size+margin), cube_initial_y+row*(cube_size+margin), cube_size, cube_size))
                        count += 1

            if count == self.current_count:
                if self.count_down == 0:
                    self.current_count += 1
                    self.count_down = 20
                self.countDown()
                break

    def checkResult(self):
        solution = self.hw1_solution(self.level)
        if len(solution) != len(self.student_output):
            return False
        for i in range(len(solution)):
            if solution[i] != self.student_output[i]:
                return False
        return True


    def hw1_solution(self, level):
        result = []
        for i in range(level):
            row = ""
            for j in range(level-i):
                row += " "
            for j in range(i*2+1):
                row += "*"
            result.append(row)
        return result
    
                