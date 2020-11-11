import pygame as pg 
import os

FPS = 60
WIDTH, HEIGHT = 1200, 675
PLAYER_WIDTH, PLAYER_HEIGHT = 163, 273

BG0 = pg.transform.scale(pg.image.load(os.path.join("assets","background.png")),(WIDTH,HEIGHT))
BG1 = pg.transform.scale(pg.image.load(os.path.join("assets","background1.png")),(WIDTH,HEIGHT))
PLAYER_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","trau.png")),(PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_VELOCITY = 5

CONVERSATION_STATE = 0
RUN_CHALLENGE_STATE = 1
FINISH_STATE = 2
#initialize pygame
pg.init()
font = pg.font.SysFont("comicsans", 50)