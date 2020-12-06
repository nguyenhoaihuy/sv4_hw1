import pygame
import time
logo = pygame.image.load('assets/logo.png') # our happy blue protagonist

def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)
        


def start_intro(screen, width, height):
        # here comes the protagonist
        opac = 0
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        
        for i in range(128):
            opac += 5
            screen.blit(background, (0, 0))
            blit_alpha(screen, logo,((width/2)-(logo.get_width()/2),(height/2)-(logo.get_height()/2)),opac)
            time.sleep(0.05)
            pygame.display.flip()
