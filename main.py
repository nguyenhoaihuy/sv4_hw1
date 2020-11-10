import pygame as pg 
import os
import time
import random
from const import *
from player import Player
from challenge1 import Challenge1

#initialize pygame
pg.init()

#create screen
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Kim Tu Thap")



#main function
def main():
    run = True
    clock = pg.time.Clock()
    #set score
    score = 0
    #challenge number
    challenge_num = 0
    #create player
    player = Player(20,HEIGHT-PLAYER_HEIGHT-10,PLAYER_IMG)
    # add random an enemy
    challenges = []
    challenges.append(Challenge1())
    
    # clean all enemy out of window
    def cleanEnemy(): # NO NEED FOR THIS
        pass
        #nonlocal enemies
        #enemies = list(filter(lambda enemy: enemy.y < HEIGHT,enemies))

    # main function to redraw all objects
    def redraw_window():
        if challenge_num == 0:
            WIN.blit(BG0,(0,0))
            player.move(WIN)
        else:
            WIN.blit(BG1,(0,0))
            challenges[0].do_challenge(WIN)

        
    #     addEnemy()
    #     #draw score and health
    #     score_text = main_font.render(f"score: {score}", 1, (255, 255, 255))
    #     hp_text = main_font.render(f"health: {player.health}", 1, (255, 255, 255))

    #     WIN.blit(score_text, (10, 10))
    #     WIN.blit(hp_text, (WIDTH - hp_text.get_width() - 10, 10))

    #     for enemy in enemies:
    #         enemy.move(WIN)
    #     #cleanEnemy()
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
        if keys[pg.K_RIGHT] and player.x + PLAYER_VELOCITY < WIDTH-PLAYER_WIDTH:
            player.x += PLAYER_VELOCITY

        if player.x >= WIDTH-300:
            challenge_num = 1
main()
