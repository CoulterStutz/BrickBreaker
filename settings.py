import pygame

screen_width = 1200
screen_height = 800     # Display
bg_color = (32, 32, 32)

player_speed = 12
player_lives = 1  # Player Settings
player_hitpoint = 100
score = 0

ball_speed = 1.0
ball_width = 3
ball_height = 15
ball_fall_rate = 1
ball_color = (60, 60, 60)
ball_image = "assets/ball.png"

brick1_image = "assets/red_brick.png"
brick2_image = "assets/blue_brick.png"
brick3_image = "assets/green_brick.png"
brick4_image = "assets/orange_brick.png"    # Brick Settings
brick5_image = "assets/pink_brick.png"
brick6_image = "assets/yellow_brick.png"

level = ["oooooooooooooooooooooo",
         "oxxxxxxxxxxxxxxxxxxxxo",
         "oxxxxxxxxxxxxxxxxxxxxo",
         "oxxxxxxxxxxxxxxxxxxxxo",
         "oxxxxxxxxxxxxxxxxxxxxo",
         "oxxxxxxxxxxxxxxxxxxxxo",
         "ooooooooooxooooooooooo"]



x_ajust_rate = 50
y_ajust_rate = 30
