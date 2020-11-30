import pygame as pg
import os
import time
import random
from const import *
from player import Player
from challenges.challenge1 import Challenge1
from challenges.lec1 import Lecture11, Lecture12

#create screen
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("CS FOUNDATION")

class Lesson1Game:
    def __init__(self, lecture1_challenge1_solution, lecture1_challenge2_solution, lecture1_homework1_solution):
        self.challenges = [
                Lecture11(),
                Lecture12(),
                Challenge1()
        ]

    def start(self):
        global main_background_state
        main_background_state = IDLE_STATE

        run = True
        clock = pg.time.Clock()
        #main background
        is_main_background = True

        #set score
        score = 0
        # is moving
        is_moving = False
        #challenge number
        current_challenge = 0
        #create player
        player = Player(20,HEIGHT-PLAYER_HEIGHT-10,PLAYER_IMG)

        # main function to redraw all objects
        def redraw_window():
            global main_background_state
            if is_main_background:
                WIN.blit(BG0,(0,0))
                player.move(WIN)
            else:
                WIN.blit(BG1,(0,0))
                main_background_state = self.challenges[current_challenge].doChallenge(WIN)
            pg.display.update()

        while run:
            clock.tick(FPS)

            redraw_window()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] and player.x - PLAYER_VELOCITY > 0:
                player.x -= PLAYER_VELOCITY
                is_moving = True
            if keys[pg.K_RIGHT] and player.x + PLAYER_VELOCITY < WIDTH-PLAYER_WIDTH:
                player.x += PLAYER_VELOCITY
                is_moving = True
            if keys[pg.K_SPACE]:
                if main_background_state == PASSED_CHALLENGE:
                    is_main_background = True
                    main_background_state = IDLE_STATE
                    current_challenge += 1
                    is_moving = False
                if main_background_state == FAILED_CHALLENGE:
                    is_main_background = True
                    self.challenges[current_challenge].reset()
                    player.x = 20
                    player.y = HEIGHT-PLAYER_HEIGHT-10
                    is_moving = False


            if is_moving and player.x >= WIDTH-950 and current_challenge == 0:
                is_main_background = False

            if is_moving and player.x >= WIDTH-700 and current_challenge == 1:
                is_main_background = False

            if is_moving and player.x >= WIDTH-450 and current_challenge == 2:
                is_main_background = False
