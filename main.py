import pygame as pg 
import os
import time
import random
from const import *
from player import Player
from challenge1 import Challenge1
from lec1 import Lecture11, Lecture12
from door import Door
from ground import Ground

#create screen
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("CS FOUNDATION")

#main function
def main():
    global main_background_state
    main_background_state = IDLE_STATE

    run = True
    clock = pg.time.Clock()
    #main background
    is_main_background = True
    
    #Press Return
    isReturnPressed = False
    
    #Open door first time
    isFirstOpen = False
    
    #set score
    score = 0
    # is moving
    is_moving = False
    #challenge number
    current_challenge = 0
    #create player
    player = Player(20,250,PLAYER_IMG)
    #create doors
    door1 = Door(250,400,CLOSE_DOOR_IMG,1)
    door2 = Door(500,400,CLOSE_DOOR_IMG,2)
    door3 = Door(750,400,CLOSE_DOOR_IMG,3)
    door4 = Door(1000,400,CLOSE_DOOR_IMG,4)
    door5 = Door(375,200,CLOSE_DOOR_IMG,5)
    door6 = Door(625,200,CLOSE_DOOR_IMG,6)
    door7 = Door(875,200,CLOSE_DOOR_IMG,7)
    #create grounds
    ground1 = Ground(0,560,GROUND1)
    ground2 = Ground(355,355,GROUND2)
    ground3 = Ground(605,355,GROUND2)
    ground4 = Ground(855,355,GROUND2)
    # add challenges
    challenges = []
    challenges.append(Lecture11())
    challenges.append(Lecture12())
    challenges.append(Challenge1())
    #add grounds
    grounds = []
    grounds.append(ground1)
    grounds.append(ground2)
    grounds.append(ground3)
    grounds.append(ground4)
    #add doors
    doors = []
    doors.append(door1)
    doors.append(door2)
    doors.append(door3)
    doors.append(door4)
    doors.append(door5)
    doors.append(door6)
    doors.append(door7)
    
    # main function to redraw all objects
    def redraw_window():
        global main_background_state
        if is_main_background:
            WIN.blit(BG0,(0,0))
            for ground in grounds:
                ground.move(WIN)
            for door in doors:
                door.move(WIN)
            player.move(WIN,grounds)
        else:
            WIN.blit(BG1,(0,0))
            main_background_state = challenges[current_challenge].doChallenge(WIN)
        pg.display.update()

    while run:
        clock.tick(FPS)

        redraw_window()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and player.x - PLAYER_VELOCITY > 0:
            player.goLeft()
            is_moving = True
        if keys[pg.K_RIGHT] and player.x + PLAYER_VELOCITY < WIDTH-PLAYER_WIDTH:
            player.goRight()
            is_moving = True
            
        
        if keys[pg.K_SPACE]:
            if is_main_background:
                player.jump()
            else:
                if main_background_state == PASSED_CHALLENGE:
                    is_main_background = True
                    main_background_state = IDLE_STATE
                    current_challenge += 1
                    is_moving = False
                if main_background_state == FAILED_CHALLENGE:
                    is_main_background = True
                    challenges[current_challenge].reset()
                    player.x = 20
                    player.y = HEIGHT-PLAYER_HEIGHT-10
                    is_moving = False
        
        if is_moving and door1.isOpened and current_challenge == 0:
            is_main_background = False
        
        if is_moving and door2.isOpened and current_challenge == 1:
            is_main_background = False

        if is_moving and door3.isOpened and current_challenge == 2:
            is_main_background = False
            
        if is_main_background:
            if keys[pg.K_RETURN]:
                if not(isReturnedPressed):
                    isReturnedPressed = True
                    for door in doors:
                        if player.isCollidedWith(door):
                            if (door.isOpened):
                                door.closeIt()
                            else:
                                door.openIt()
                                delta = door.x + DOOR_CLOSED_WIDTH/2 - (player.x + PLAYER_WIDTH/2)
                                while abs(delta) > 3:
                                    if delta < 0:
                                        player.x -= 2
                                    else:
                                        player.x += 2
                                    delta = door.x + DOOR_CLOSED_WIDTH/2 - (player.x + PLAYER_WIDTH/2)
                                    redraw_window()
                                time.sleep(0.5)
            else:
                isReturnedPressed = False
        

main()
