import pygame

from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, PADDING, PLAYER1, PLAYER2

class Board:
    def __init__(self):
        self.board = []
        self.make_emptyboard()
        self.x = 0
        self.y = 0
         
    def calc_pos(self, row, col):
        self.x = int(SQUARE_SIZE * col + SQUARE_SIZE // 2)
        self.y = int(SQUARE_SIZE * row + SQUARE_SIZE // 2)
        
    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE + PADDING*row , col * SQUARE_SIZE + PADDING * col , SQUARE_SIZE  , SQUARE_SIZE  ))
    def make_emptyboard(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)
    def make_move(self, turn, row, col, win):
        self.calc_pos(row, col)  
        if self.board[row][col] == 0:
            if turn == PLAYER1:
                self.board[row][col] = 'X'
                rect = pygame.Rect(self.x- int(SQUARE_SIZE/4), self.y-int(SQUARE_SIZE/4), SQUARE_SIZE//2, SQUARE_SIZE//2)
                pygame.draw.rect(win, RED, rect)
            elif turn == PLAYER2:
                radius = int(SQUARE_SIZE//4)
                self.board[row][col] = 'O'
                pygame.draw.circle(win, RED, (self.x, self.y), radius)
            return True
        else:
            return False
        print(row, col,self.board, 'LLEGO AQUI')

