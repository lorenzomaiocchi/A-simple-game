import pygame




class Player:
    def __init__(self, x_pos, y_pos, sg_game):
        
        #position in the game window
        self.screen = sg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.color = (0, 50 , 224)
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x_pos, self.y_pos, 50, 50] )
    

    def move_right(self):
        self.x_pos += 5

    def move_left(self):
        self.x_pos -= 5
    
    def jump(self):
        pass