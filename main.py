import pygame
from settings import Settings
import sys

from characters import Player






class GAME:

    def __init__(self):
        pygame.init()
        self.clock  = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.window_dimensions)
        pygame.display.set_caption('A simple game')
        


        #Characters

        self.Player = Player( x_pos= 100, y_pos= 200, sg_game= self)

    


    def run_game(self):

        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
        

            

            

    def _check_events(self):
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
        

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.Player.move_right()
        
        if keys[pygame.K_a]:
            self.Player.move_left()
    
    def _update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.Player.draw()
        pygame.display.flip()
         









if __name__ == '__main__':
    sg = GAME()

    sg.run_game()
