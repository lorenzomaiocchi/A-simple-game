import pygame
import random

class Entity:

    def __init__(self, sg_game):
        
        #position in the game window
        self.screen = sg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.color = (250, 0 , 224)


        self.pos_x = random.randint(400, 800)
        self.pos_y = 320
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 50, 50)

    def update(self, game_speed = 10):

        self.pos_x -= game_speed

        if self.pos_x <= -self.screen_rect.width:

            self.pos_x = random.randint(810, 825)
            self.pos_y = random.randint(310, 330)

    def draw(self):
        self.rect.topleft = (self.pos_x, self.pos_y)
        pygame.draw.rect(self.screen, self.color, self.rect)
    