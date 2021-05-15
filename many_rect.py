"""
Generates and maintains N rectangles
Author: Samuel Rodriguez (sar325@cornell.edu)
Last Updated: 05/15/21
"""
import pygame
from constants import *
import random


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


def draw_rect(rect, color, window):
    """
    draws one rectangle [rect] with [color] on [window]
    """
    pygame.draw.rect(window, color, rect)


def draw_rects(rect_objs, window):
    """
    draws many rectangles in [rect_objs] with its
    associated color if it is visible on [window]
    """
    for shape in rect_objs:
        if shape['visible']:
            rect = shape['rect']
            color = shape['color']
            draw_rect(rect, color, window)


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
