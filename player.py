"""
This module contains class Player

Author: Samuel Rodriguez (sar325@cornell.edu)
Last Updated: 05/15/21
"""
from character import Character
import pygame
from constants import *
from clock import Clock

# TODO: Collision detection between bullets and objects on screen

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

    def __init__(self, clock, left=0, top=0, width=10, height=10, velocity=[1, 1]):
        """
        Initializes a `Player`.
        Defaults: (**left**, **top**) = (0, 0); (**width**, **height**) = (10, 10);
            **velocity** = [1, 1]

        Parameter **clock**: the timekeeper
        Precondition: **clock** must be of type Clock

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
            assert isinstance(clock, Clock), "Player clock must be a Clock"
        super().__init__()
        self._left = left
        self._top = top
        self._width = width
        self._height = height
        self._velocity = velocity
        self._rect = pygame.Rect(left, top, width, height)
        self._clock = clock
        self._shoot_clock = Clock(clock._fps, SHOOT_COOLDOWN)
        self._bullets = []

    def shoot(self, speed=BULLET_SPEED, size=(BULLET_SIZE, BULLET_SIZE), color=BULLET_COLOR):
        """
        if spacebar was pressed, shoots a `Bullet` from `Player` moving
        at a **velocity** with **size** and **color** attributes.

        Parameter **size**: the size of the `Bullet`
        Precondition: **size** is a tuple pair (width, height) of floats

        Parameter **speed**: the speed of the `Bullet`
        Precondition: **speed** is a float

        Parameter **color**: the color of the `Bullet`
        Precondition: **color** is the color of the bullet
        """
        # TODO: Make shoot directions more ergonomic
        keys = pygame.key.get_pressed()
        if keys[SHOOT_KEY]:
            if self._shoot_clock._cool_clock > self._shoot_clock.cooldown_time():
                self._shoot_clock.reset_cooldown()
                velocity = [0, 0]
                if keys[SHOOT_UP]:
                    velocity[1] = -speed
                if keys[SHOOT_DOWN]:
                    velocity[1] = speed
                if keys[SHOOT_LEFT]:
                    velocity[0] = -speed
                if keys[SHOOT_RIGHT]:
                    velocity[0] = speed
                if velocity != [0, 0]:
                    self._create_bullet(size, velocity, color)

    def _create_bullet(self, size, velocity, color):
        """
        Creates `Bullet` with **size**, **velocity**, and **color** and adds
        it to the bullets list
        """
        shape = pygame.Rect(self._rect.centerx,
                            self._rect.centery, size[0], size[1])
        bullet = {'velocity': velocity, 'rect': shape,
                  'color': color, 'visible': True}
        self._bullets.append(bullet)

    def _is_visible(self, obj):
        """
        True if **obj** is within the **window**. False otherwise
        """
        # TODO: FINISH THIS
        window_w = SCREEN_W
        window_h = SCREEN_H
        return obj.right >= 0 and obj.left <= window_w and obj.top >= 0 and obj.bottom <= window_h

    def _draw_bullets(self, window):
        """
        draws all bullets that are visible. Sets their visibility off if the
        bullet is not in the window
        """
        for bullet in self._bullets:
            if not self._is_visible(bullet['rect']):
                bullet['visible'] = False
            if bullet['visible']:
                pygame.draw.rect(window, bullet['color'], bullet['rect'])
        self._bullets = [
            bullet for bullet in self._bullets if bullet['visible']]

    def _move_bullets(self):
        for bullet in self._bullets:
            bullet['rect'].move_ip(bullet['velocity'][0],
                                   bullet['velocity'][1])

    def draw(self, window, color=BLACK):
        """
        Draws `Player` with **color ** on ** window**

        Parameter ** color**: the color to draw[player]
        Precondition: **color ** is an RGB tuple
        Default: **color ** is BLACK
        """
        assert type(color) == tuple, "color is not a tuple"
        for v in color:
            assert v >= 0 and v <= 255, "each val in color must be a valid RGB value"
        pygame.draw.rect(window, color, self._rect)
        self._draw_bullets(window)

    def move(self):
        """
        Moves `Player` at ** velocity ** if the player used any directional key.
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
        Moves `Player` at ** velocity ** if the player used any directional key.
        Shoots laser beam if `Player` pressed SHOOT_KEY
        """
        keys = pygame.key.get_pressed()
        self.move()
        self._move_bullets()
        self.shoot()
        self._shoot_clock.update()
