import pygame
from settings import Settings, Background
import sys
import os
import time

from characters import Player
from obstacles import Entity






class GAME:

    def __init__(self):
        pygame.init()
        self.clock  = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.window_dimensions)
        pygame.display.set_caption('A simple game')
        self.BG = Background(self)

        self.score = 0
        self.font = pygame.font.SysFont(None, 30)
       
        

    

        


        #Characters

        self.Player = Player( x_pos= 50, y_pos= 320, sg_game= self)
        self.Entities = [Entity(self) for _ in range(2)]

    


    def run_game(self):

        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(30)

            self.score += 1
        

            

            

    def _check_events(self):
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
        

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and not self.Player.jumping:
            self.Player.start_jump()
    
    def _update_screen(self):
        self.BG.drawBG()
        self.Player.update_jump()
        self.Player.draw()
        self.text_score = self.font.render("Points: " + str(self.score), True, (0, 0, 0))
        self.textRect = self.text_score.get_rect()
        self.textRect.center = (650, 25 )
        self.screen.blit(self.text_score, self.textRect)
       
       
       
        for entity in self.Entities:
            entity.draw()
            entity.update()
            if self.Player.rect.colliderect(entity.rect):
                self.Player.color = (250, 0, 0)
                text = pygame.font.SysFont(None, 48)

                game_over_text = text.render('Game Over', True, (0, 0, 0))
                text_rect = game_over_text.get_rect(center=self.screen.get_rect().center)
                self.screen.blit(game_over_text, text_rect)
                self.score = 0




            
            
        pygame.display.flip()
         









if __name__ == '__main__':
    sg = GAME()

    sg.run_game()
