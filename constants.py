from colors import *
from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE, K_w, K_a, K_s, K_d
# Screen attributes
SCREEN_W, SCREEN_H = 1440, 720
FPS = 60
# Physics attributes
COLLISION = True
P_COLLISION = True
SPAWN_N = 10
# Player attributes
P_COLOR_ALPHA = SAFFRON
P_COLOR_BETA = RED
P_VELOCITY = [3, 3]
P_W = 50
P_H = 50
P_SPAWN_X = SCREEN_W / 2
P_SPAWN_Y = SCREEN_H / 2
SHOOT_KEY = K_SPACE
SHOOT_COOLDOWN = 20  # milliseconds
MOVE_UP = K_UP
MOVE_DOWN = K_DOWN
MOVE_LEFT = K_LEFT
MOVE_RIGHT = K_RIGHT
SHOOT_UP = K_w
SHOOT_LEFT = K_a
SHOOT_DOWN = K_s
SHOOT_RIGHT = K_d
# Bullet attributes
BULLET_SPEED = 10
BULLET_SIZE = 10
BULLET_COLOR = BLACK
