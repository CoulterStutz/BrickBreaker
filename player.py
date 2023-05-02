import pygame, settings

class Player:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_left = False
        self.moving_right = False

        self.x = float(self.rect.x)

    def update(self):

        self.rect.y = 700

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += settings.player_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= settings.player_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
