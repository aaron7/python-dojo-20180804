import unittest
from unittest.mock import patch

from simple import run

class TestSimple(unittest.TestCase):

    def test_voting(self):
        user_input = [
            "Dojo Website",
            "Minesweepers",
            "Rocker paper scissors AI",
            "Pickle sanitiser",
            "Face swap",
            "Space simulator",
            "FINISH",

            "4", # Dojo website
            "8", # Minesweepers
            "8", # Rocker paper scissors AI
            "2", # Pickle sanitiser
            "0", # Face swap
            "9", # Space simulator

            "12", # Minesweepers
            "8", # Rocker paper scissors AI
            "2", # Space simulator
        ]

        with patch('builtins.input', side_effect=user_input):
            run()

if __name__ == '__main__':
    unittest.main()