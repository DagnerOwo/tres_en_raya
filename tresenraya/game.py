import pygame
from .constants import RED, WHITE, BLACK, SQUARE_SIZE, PLAYER1, PLAYER2
from .board import Board
from tkinter import *
from tkinter import messagebox

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.turn = PLAYER1
        self.board.draw_squares(self.win)
    def update(self):
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
    def select(self, row, col):
        if self.board.make_move(self.turn, row, col, self.win):
            winner = self.check_winner()
            if  winner != None:
                Tk().wm_withdraw() #to hide the main window
                pygame.display.update()
                messagebox.showinfo('GRATS!','El ganador es el {}'.format(winner))
                pygame.quit()
            self.change_turn()
    def change_turn(self):
        if self.turn == PLAYER1:
            self.turn = PLAYER2
        else:
            self.turn = PLAYER1
    def check_winner(self):
        win = None
        #horizontal line
        for i in range(len(self.board.board)):
            winner_moves = list(filter(lambda piece: piece == self.turn, self.board.board[i]))
            if len(winner_moves) == 3:
                win = self.turn
        #vertical line
        for i in range(len(self.board.board)):
            count = 0
            for k in range(len(self.board.board[i])):
                if self.board.board[k][i] == self.turn:
                    count +=1
            if count == 3:
                win = self.turn
        #diagonal line from left to right
        count = 0
        for i in range(len(self.board.board)):
            if self.board.board[i][i] == self.turn:
                count += 1
                print(count, 'Counter')
            if count == 3:
                win = self.turn
        #diagonal line from right to left
        count = 0
        for i in reversed(range(len(self.board.board))):
            length = len(self.board.board) -1
            if self.board.board[length-i][i] == self.turn:
                count +=1
            if count == 3:
                win = self.turn
        return win
