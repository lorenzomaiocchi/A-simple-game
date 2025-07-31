import pygame
import sys
import os
import random



BGCOLOR = (250, 250, 250)

WIDTH = 300
HEIGHT = 600

pygame.init()

BG = pygame.image.load(os.path.join('Images\Other', 'Back.png'))
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))


class Player:
    


    def __init__(self, game_screen):
        
        self.screen = game_screen
        self.color  = (250, 0, 0)
        self.screen_rect = game_screen.get_rect()
        self.pos_x = WIDTH//2
        self.pos_y =    HEIGHT - 40

        self.image = pygame.Rect(self.pos_x, self.pos_y, 10, 20)

        self.velocity = 5

    def draw(self):
        
        pygame.draw.rect(self.screen, self.color, self.image)

    def update(self, UserInput):

        if UserInput[pygame.K_a]:

            self.image.x -= self.velocity
        if UserInput[pygame.K_d]:

            self.image.x += self.velocity
        


bg_x_pos = 0
bg_y_pos = -250




def game():


    game_speed = 20



    run = True
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    ship = Player(SCREEN)

    clock  = pygame.time.Clock()



    def window():
        global bg_x_pos, bg_y_pos

       
        Image_H = BG.get_height()

        SCREEN.blit(BG, (bg_x_pos, bg_y_pos))
        SCREEN.blit(BG, (bg_x_pos, bg_y_pos + Image_H))
        
        if bg_y_pos <=  -Image_H:
            SCREEN.blit(BG, (bg_x_pos, Image_H + bg_y_pos))
            bg_y_pos = 0
        
        bg_y_pos -= game_speed




        
        

    while run:
        for event in pygame.event.get():

    

            if event.type == pygame.QUIT:
                
                sys.exit()
        
        keys = pygame.key.get_pressed()


        window()
        ship.draw()
        ship.update(keys)
        
        pygame.display.flip()
        clock.tick(30)


    


    




        



game()