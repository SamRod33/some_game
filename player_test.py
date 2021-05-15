"""
This file contains the Player module test suite

Author: Samuel Rodriguez (sar325@cornell.edu)
Last Updated: 05/15/21
"""
import unittest
from player import Player
from pygame import Rect


class TestSuite(unittest.TestCase):
    def test_p_initalize(self):
        """
        Tests if a player is initalized correctly
        """
        player = Player(0, -10, 2, 1, [1, 1])
        self.assertEqual(player._left, 0, "Player Left = 0")
        self.assertEqual(player._top, -10, "Player Top = -10")
        self.assertEqual(player._height, 1, "Player Height = 1")
        self.assertEqual(player._width, 2, "Player Width = 2")
        self.assertEqual(player._velocity, [1, 1], "Player Velocity = [1, 1]")
        rect = Rect(0, -10, 2, 1)
        self.assertEqual(player._rect, rect, "Player Rect is rect")


if __name__ == '__main__':
    unittest.main()
