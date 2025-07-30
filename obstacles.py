import pygame
import random

class Entity:

    def __init__(self, sg_game):
        
        #position in the game window
        self.screen = sg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.color = (250, 0 , 224)


        self.pos_x = random.randint(250, 350)
        self.pos_y = random.randint(100, 250)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.pos_x, self.pos_y, 50, 50] )
    