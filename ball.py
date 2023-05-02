import pygame, settings, ball_math
import random

class Ball:

    def __init__(self, ai_game, spawn_x=None, spawn_y=650):

        self.spawn_x = spawn_x
        self.spawn_y = spawn_y
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("assets/ball.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_left = False
        self.moving_right = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def hit(self):
        self.x = random.randint(-6, 6) * 100
        self.y = random.randint(-6, 6) * 100

    def update(self):

        self.rect.y = self.spawn_y
        if self.spawn_x == None:
            self.rect.x = self.x
        else:
            self.rect.x = self.spawn_x

    def reset(self):
        self.posx = 0
        self.posy = 600
        self.xFac, self.yFac = 1, -1
  
    # Used to change the direction along Y axis


    def blitme(self):
        self.screen.blit(self.image, self.rect)
