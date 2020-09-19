import pygame
from .constants import BACKGROUND_RED, BACKGROUND_WHITE, BACKGROUND_BLACK, SQUARE_SIZE
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw_squares(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BACKGROUND_RED
        