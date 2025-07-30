import pygame
import os

class Settings:

    def __init__(self):

        self.window_dimensions = (800, 400)

        self.background_color = (255, 255, 255)


 


class Background:
    

    def __init__(self, sg_game):

        
        self.screen = sg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(os.path.join('Images\Other', 'background.bmp'))
        self.bg_width = self.image.get_width()
        self.x_pos_bg = 0
        self.y_pos_bg = 0

        

    
    def drawBG(self, game_speed = 20):
        
        self.screen.blit(self.image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(self.image, (self.x_pos_bg + self.bg_width, self.y_pos_bg))



        if self.x_pos_bg <= - self.bg_width:
            self.screen.blit(self.image, (self.bg_width+ self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        
        self.x_pos_bg -= game_speed

