# main.py

"""
This file is not necessary for python, but other languages require a main file.
The __main__ file is the file that the user is supposed to run.
"""
from c_game_engine import Game

class Main:
    def __init__(self):
        self.GAME = Game()
        self.GAME.setup()
        self.GAME.run()

"""
functionally:
def Main():
    GAME = Game()
    GAME.setup()
    GAME.run()
"""

if __name__ == "__main__":
    Main()