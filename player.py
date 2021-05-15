"""
This module contains class Player

Author: Samuel Rodriguez (sar325@cornell.edu)
Last Updated: 05/15/21 
"""
from character import Character
import pygame
from constants import *

# whether to check for preconditions
_prec = True


def _assert_int_float(v, module="player"):
    """
    asserts [v] is an int or float inside module
    """
    assert type(v) == int or type(v) == float, \
        (str(module) + " attr must be of type int")


class Player(Character):
    """
    Module `Player` is the representation of a player character in a game.
    """

    def __init__(self, left: float = 0, top=0, width=10, height=10, velocity=[1, 1]):
        """
        Initializes a `Player`.
        Defaults: (**left**, **top**) = (0, 0); (**width**, **height**) = (10, 10);
            **velocity** = [1, 1]

        Parameter **left**: the left edge pixel to spawn the `Player` 
        Precondition: **left** is an int/float

        Parameter **top**: the top edge pixel to spawn the `Player` 
        Precondition: **top** is an int/float

        Parameter **width**: the width of the `Player`
        Precondition: **width** is an int/float >= 0

        Parameter **height**: the height of the `Player` 
        Precondition: **height** is an int/float >= 0

        Parameter **velocity**: the velocity the player moves
        Precondition: **velocity** is a list of int/float of length 2
        """
        if _prec:
            is_ints = [left, top, width, height]
            for attr in is_ints:
                _assert_int_float(attr)
            assert width >= 0 and height >= 0, "Player width and height must be >= 0"
            assert type(velocity) == list, \
                "Player velocity must be of type list"
            for v in velocity:
                _assert_int_float(attr)
        super().__init__()
        self._left = left
        self._top = top
        self._width = width
        self._height = height
        self._velocity = velocity
        self._rect = pygame.Rect(left, top, width, height)

    # def shoot(rect, velocity, size, color):
    #     """
    #     Shoots a bullet from [rect] moving with [direction], [size] and [color]
    #     if spacebar was pressed.
    #     """
    #     keys = pygame.key.get_pressed()
    #     if keys[SHOOT_KEY] and clock.cooldown_time() >= SHOOT_COOLDOWN:
    #         clock.reset_cooldown()
    #         print("Pew")
    #     bullet = pygame.Rect(self._rect.x, self._rect.y, size, size)
    #     # TODO: FINISH BULLET INCLUSION

    def draw(self, window, color=BLACK):
        """
        Draws `Player` with **color** on **window**

        Parameter **color**: the color to draw [player]
        Precondition: **color** is an RGB tuple
        Default: **color** is BLACK
        """
        assert type(color) == tuple, "color is not a tuple"
        for v in color:
            assert v >= 0 and v <= 255, "each val in color must be a valid RGB value"
        pygame.draw.rect(window, color, self._rect)

    def move(self):
        """
        Moves `Player` at **velocity** if the player used any directional key.
        """
        keys = pygame.key.get_pressed()
        if keys[MOVE_LEFT] and not self._rect.left <= 0:
            self._rect.move_ip(-self._velocity[0], 0)
        if keys[MOVE_RIGHT] and not self._rect.right >= SCREEN_W:
            self._rect.move_ip(self._velocity[0], 0)
        if keys[MOVE_UP] and not self._rect.top <= 0:
            self._rect.move_ip(0, -self._velocity[1])
        if keys[MOVE_DOWN] and not self._rect.bottom >= SCREEN_H:
            self._rect.move_ip(0, self._velocity[1])

    def action(self):
        """
        Moves `Player` at **velocity** if the player used any directional key.
        Shoots laser beam if `Player` pressed SHOOT_KEY
        """
        keys = pygame.key.get_pressed()
        self.move()
        # self.shoot()
