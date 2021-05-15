import pygame


class Clock():

    def __init__(self, FPS, COOLDOWN_TIMER):
        """
        creates a clock that keeps track of time. 
        FPS is the frames per second the clock will tick at.
        """
        self._global_time = 0
        self._clock = pygame.time.Clock()
        self._fps = FPS
        self._cooldown = COOLDOWN_TIMER

    def update(self):
        """
        Updates global time and ticks the clock forward
        """
        dt = self._clock.tick(self._fps)
        self._global_time += dt
        self._cooldown += dt

    def global_time(self):
        """
        Gets the total amount of time that has passed since this clock's creation
        """
        return self._global_time

    def cooldown_time(self):
        return self._cooldown

    def reset_cooldown(self):
        self._cooldown = 0
