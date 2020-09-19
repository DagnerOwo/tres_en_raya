import pygame

from .constants import BACKGROUND_BLACK, ROWS, BACKGROUND_RED, SQUARE_SIZE, COLS, BACKGROUND_WHITE, PADDING

class Board:
    def __init__(self):
        self.board = []
        
    def draw_squares(self, win):
        win.fill(BACKGROUND_WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BACKGROUND_BLACK, (row*SQUARE_SIZE + PADDING*row , col * SQUARE_SIZE + PADDING * col , SQUARE_SIZE  , SQUARE_SIZE  ))

    