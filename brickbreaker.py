import pygame
from player import Player
from ball import Ball
import os, sys
import settings


class BrickBreaker:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

        pygame.display.set_caption("Brickbreaker!")
        self.screen.fill(settings.bg_color)

        self.player = Player(self)
        self.to_spawn_bricks = []
        self.bricks = []

        self.balls = []
        self.ball = Ball(self)
        self.balls.append(self.ball)


    def run_game(self):

        self.generate_bricks()

        while True:
            self.check_events()
            self.update_screen()

    def update_screen(self):

        self.update_bricks()
        self.update_balls()
        self.update_player()

        pygame.display.flip()
        self.screen.fill(settings.bg_color)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.player.moving_left = True
                elif event.key == pygame.K_0:
                    self.ball.hit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.player.moving_left = False
        
        point_player_x = self.player.x
        point_ball_x = self.ball.x
        point_ball_y = self.ball.y

        if point_player_x - point_ball_x <= settings.player_hitpoint and point_player_x - point_ball_x >= settings.player_hitpoint * -1:
            # do collide stuff
            None
        else:
            None


    def generate_bricks(self):
        bricks = '\n'.join(settings.level).split()
        row = 0
        column = 0
        brick_x = int
        brick_y = int

        for x in bricks:
            row += 1
            column = 0
            for y in x:
                column += 1
                if y == "r":
                    brick_x = column * settings.x_ajust_rate
                    brick_y = row * settings.y_ajust_rate
                    brick = {'x': brick_x, 'y': brick_y, 'image': settings.brick1_image}
                    self.to_spawn_bricks.append(brick)
                elif y == "g":
                    brick_x = column * settings.x_ajust_rate
                    brick_y = row * settings.y_ajust_rate
                    brick = {'x': brick_x, 'y': brick_y, 'image': settings.brick3_image}
                    self.to_spawn_bricks.append(brick)
                elif y == "b":
                    brick_x = column * settings.x_ajust_rate
                    brick_y = row * settings.y_ajust_rate
                    brick = {'x': brick_x, 'y': brick_y, 'image': settings.brick2_image}
                    self.to_spawn_bricks.append(brick)
                elif y == "p":
                    brick_x = column * settings.x_ajust_rate
                    brick_y = row * settings.y_ajust_rate
                    brick = {'x': brick_x, 'y': brick_y, 'image': settings.brick5_image}
                    self.to_spawn_bricks.append(brick)
                elif y == "o":
                    brick_x = column * settings.x_ajust_rate
                    brick_y = row * settings.y_ajust_rate
                    brick = {'x': brick_x, 'y': brick_y, 'image': settings.brick4_image}
                    self.to_spawn_bricks.append(brick)
                elif y == "y":
                    brick_x = column * settings.x_ajust_rate
                    brick_y = row * settings.y_ajust_rate
                    brick = {'x': brick_x, 'y': brick_y, 'image': settings.brick6_image}
                    self.to_spawn_bricks.append(brick)
                elif y == "x":
                    None

    def spawn_ball(self):
        None

    def update_balls(self):
        for x in self.balls:
            x.blitme()
            x.update()

    def update_bricks(self):
            for brick in self.to_spawn_bricks:
                self.screen.blit(pygame.transform.scale(pygame.image.load(brick['image']), (40, 20)), (brick["x"], brick["y"]))

    def update_player(self):
        self.player.blitme()
        self.player.update()

if __name__ == "__main__":
    BrickBreaker().run_game()
