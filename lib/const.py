import pygame as pg 
import os

FPS = 60
WIDTH, HEIGHT = 1200, 675
PLAYER_WIDTH, PLAYER_HEIGHT = 130, 218
NPC_WIDTH, NPC_HEIGH = 163, 273
NPC_X = 150
NPC_Y = HEIGHT - NPC_HEIGH - 50

BG0 = pg.transform.scale(pg.image.load(os.path.join("assets","background.png")),(WIDTH,HEIGHT))
BG1 = pg.transform.scale(pg.image.load(os.path.join("assets","background1.png")),(WIDTH,HEIGHT))
PLAYER_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","trau.png")),(PLAYER_WIDTH, PLAYER_HEIGHT))
TRAU_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","trau.png")),(NPC_WIDTH, NPC_HEIGH))
AI_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","tre.png")),(NPC_WIDTH, NPC_HEIGH))
PLAYER_VELOCITY = 5

CONVERSATION_STATE = 0
RUN_CHALLENGE_STATE = 1
FINISH_STATE = 2
PASSED_CHALLENGE = 3
FAILED_CHALLENGE = 4
IDLE_STATE = 5

#initialize pygame
pg.init()
font = pg.font.SysFont("comicsans", 50)