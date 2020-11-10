import pygame as pg
import time
from challenge import Challenge
red = (255,0,0)
white = (255,255,255)
class Challenge1(Challenge):    
    def __init__(self):
        self.count = 0
        self.current_count = 0
        self.count_down = 20
        super().__init__()

    def do_challenge(self, window):
        output = self.student_implementation(5)
        self.count = 25
        self.draw_output(window,output)

    def draw_output(self, window,output):
        width = 650
        height = 400
        x_a = 450
        y_a = 20
        level = len(output)
        margin = 5
        cube_size = (height - 20)//(level+margin)
        cube_initial_x = x_a + width//2-level*(cube_size+margin)-cube_size//2
        cube_initial_y = y_a + height-level*(cube_size+margin)-10
        pg.draw.rect(window, white, (450, 20, width, height))
        count = 0
        for row in range(len(output)):
            for col in range(len(output[row])):
                if output[row][col] == "*":
                    if self.current_count == self.count:
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
                self.count_down_fun()

                break

    def count_down_fun(self):
        if self.count_down != 0:
            self.count_down -= 1


    def student_implementation(self, level):
        result = []
        for i in range(level):
            row = ""
            for j in range(level-i):
                row += " "
            for j in range(i*2+1):
                row += "*"
            result.append(row)
        return result
                