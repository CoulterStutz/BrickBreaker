import pygame, settings, ball_math

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

    def animate_ball_falling(self, to_y):
        fall_rate = settings.ball_fall_rate / 10

        for x in range(10):
            self.y = self.y + to_y / 10
            # pygame.time.wait(ball_math.convert_float_to_int(fall_rate))

    def update(self):

        self.rect.y = self.spawn_y
        if self.spawn_x == None:
            self.rect.x = self.x
        else:
            self.rect.x = self.spawn_x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
