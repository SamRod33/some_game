import pygame

from colors import *
from constants import *
from clock import Clock
from player import Player
from many_rect import *


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


def game_loop():
    window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    window.fill(WHITE)
    pygame.display.set_caption("Game: ")
    clock = Clock(FPS)
    running = True
    rect_objs = gen_rects(SPAWN_N)
    player = Player(clock, P_SPAWN_X, P_SPAWN_Y, P_W, P_H, P_VELOCITY)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # draw
        window.fill(WHITE)
        draw_rects(rect_objs, window)
        move_rects(rect_objs)
        if COLLISION and is_collision(player._rect, rect_objs):
            player.draw(window, P_COLOR_BETA)
        else:
            player.draw(window, P_COLOR_ALPHA)
        player.action()
        pygame.display.update()
        # update clock
        clock.update()


if __name__ == "__main__":
    game_loop()
