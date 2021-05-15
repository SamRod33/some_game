import pygame
import random

from colors import *
from constants import *
from clock import Clock
from player import Player

# TODO: Move player to its own class along with methods
# TODO: Move all rectangle functionality to its own class

window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
window.fill(WHITE)
pygame.display.set_caption("Game: ")
clock = Clock(FPS, 0)


def move_rect(rect, velocity):
    """
    moves one rectangle [rect] going at [velocity]
    """
    if rect.right > SCREEN_W or rect.left < 0:
        velocity[0] = -velocity[0]
    if rect.bottom > SCREEN_H or rect.top < 0:
        velocity[1] = -velocity[1]
    rect.move_ip(velocity[0], velocity[1])


def move_rects(rect_objs):
    """
    moves many rectangles. For each element in [rect_objs],
    we gather the rectangle and its velocity.
    """

    for shape in rect_objs:
        rect = shape['rect']
        velocity = shape['velocity']
        move_rect(rect, velocity)


def draw_rect(rect, color):
    """
    draws one rectangle [rect] with [color]
    """
    pygame.draw.rect(window, color, rect)


def draw_rects(rect_objs):
    """
    draws many rectangles in [rect_objs] with its
    associated color if it is visible
    """
    for shape in rect_objs:
        if shape['visible']:
            rect = shape['rect']
            color = shape['color']
            draw_rect(rect, color)


def gen_rects(n):
    """
    Returns a list of generated rectangles.
    n is the number of rectangles to generate.
    """
    output = []
    for i in range(n):
        rect_w = random.randint(20, 75)
        rect_h = random.randint(20, 75)
        # use rect dimensions so they do not spawn over the screen
        x = random.randint(rect_w, SCREEN_W - rect_w)
        y = random.randint(rect_h, SCREEN_H - rect_h)
        color = COLORS[random.randint(0, len(COLORS)-1)]
        velocity_x = random.randint(2, 6)
        velocity_y = random.randint(1, 6)
        new_rect_obj = {
            'rect': pygame.Rect(x, y, rect_w, rect_h),
            'color': color,
            'velocity': [velocity_x, velocity_y],
            'visible': True
        }
        output.append(new_rect_obj)
    return output


def player_action(rect, velocity):
    """
    Moves [rect] at [velocity] if the player used any directional key.
    Shoots laser beam if player pressed SHOOT_KEY
    """
    keys = pygame.key.get_pressed()
    if keys[MOVE_LEFT] and not rect.left <= 0:
        rect.move_ip(-velocity[0], 0)
    if keys[MOVE_RIGHT] and not rect.right >= SCREEN_W:
        rect.move_ip(velocity[0], 0)
    if keys[MOVE_UP] and not rect.top <= 0:
        rect.move_ip(0, -velocity[1])
    if keys[MOVE_DOWN] and not rect.bottom >= SCREEN_H:
        rect.move_ip(0, velocity[1])
    if keys[SHOOT_KEY] and clock.cooldown_time() >= SHOOT_COOLDOWN:
        clock.reset_cooldown()
        print("Pew")


def shoot(rect, velocity, size, color):
    """
    Shoots a bullet from [rect] moving with [direction], [size] and [color]
    """
    bullet = pygame.Rect(rect.x, rect.y, size, size)
    # TODO: FINISH BULLET INCLUSION


# def is_collision(rect1, rects):
#     """
#     Returns the rectangle in [rects] that collided with [rect1]. None otherwise.
#     """
#     for shape in rects:
#         rect2 = shape['rect']
#         if rect1.colliderect(rect2) and shape['visible']:
#             shape['visible'] = False
#             return rect2
#     return None


def is_collision(rect1, rects):
    """
    Returns the last rectangle in [rects] that collided with [rect1],
    None otherwise. Also changes all rectangles in [rects] that collided
    with [rect1] visibility to False.
    """
    output = None
    for shape in rects:
        rect2 = shape['rect']
        if rect1.colliderect(rect2) and shape['visible']:
            shape['visible'] = False
            output = rect2
    return output


def draw_player(player, alpha, beta, rects):
    """
    Draws [player] with [beta] if P_COLLUSION is on and if [player] collides
    with any rectangle in [rects], otherwise [player] is drawn with [alpha].
    """
    if P_COLLISION and is_collision(player, rects) is not None:
        pygame.draw.rect(window, beta, player)
    else:
        pygame.draw.rect(window, alpha, player)


def game_loop():
    running = True
    rect_objs = gen_rects(SPAWN_N)
    # player = pygame.Rect(P_SPAWN_X, P_SPAWN_Y, P_W, P_H)
    player = Player(P_SPAWN_X, P_SPAWN_Y, P_W, P_H, P_VELOCITY)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # draw
        window.fill(WHITE)
        draw_rects(rect_objs)
        move_rects(rect_objs)
        # if COLLISION:
        #     draw_player(player, P_COLOR_ALPHA,
        #                 P_COLOR_BETA, rect_objs)
        #     rect_objs = [shape for shape in rect_objs if shape['visible']]
        # else:
        #     draw_rect(player, P_COLOR_ALPHA)
        # player_action(player, P_VELOCITY)
        if COLLISION and is_collision(player._rect, rect_objs):
            player.draw(window, P_COLOR_BETA)
        else:
            player.draw(window, P_COLOR_ALPHA)
        player.action()
        pygame.display.update()
        # update clock
        clock.update()


game_loop()
