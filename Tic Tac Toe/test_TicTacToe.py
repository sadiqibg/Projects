"""

The def 

"""

import unittest
from unittest.case import TestCase 
import methods
import TicTacToe
import config


class TestMethods(unittest, TestCase):
    
    def test_place_marker(self):
        # Placing marker in spot 1
        methods.place_marker(1)
        self.assertNotEqual(config.label1.cget("text"),"")


if __name__ == '__main__':
    unittest.main()
