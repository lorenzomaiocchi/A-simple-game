import pygame




class Player:
    def __init__(self, x_pos, y_pos, sg_game):
        
        #position in the game window
        self.screen = sg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.color = (0, 50 , 224)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.jumping = False
        self.gravity_y = 2
        self.jump_vel = 25
        self.JUMP_V = self.jump_vel
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 50, 50)

    def draw(self):
        self.rect.topleft = (self.x_pos, self.y_pos) 
        pygame.draw.rect(self.screen, self.color, self.rect)

    def start_jump(self):
        if not self.jumping:
            self.jumping = True 
    def update_jump(self):
        if self.jumping:
            self.y_pos -= self.jump_vel * 1.5
            self.jump_vel -= self.gravity_y 
            if self.jump_vel < -self.JUMP_V:
                self.jumping = False
                self.jump_vel = self.JUMP_V